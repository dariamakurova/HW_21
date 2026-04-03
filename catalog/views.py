from gettext import Catalog
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, ModeratorProductForm
from catalog.models import Product


def home(request):
    return render(request, 'catalog/main.html')

class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"

# def contacts(request):
#     if request.method == 'POST':
#         # Получение данных из формы
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено. Мы скоро с вами свяжемся.")
#     return render(request, 'catalog/contacts.html')

def category_1(request):
    return render(request, 'catalog/category_1.html')

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:catalog')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    raise_exception = True

    def get_queryset(self):
        if self.request.user.has_perm('catalog.can_unpublish_product'):
            return Product.objects.all()
        return Product.objects.filter(owner=self.request.user)

    def get_form_class(self):
        if self.request.user.has_perm('catalog.can_unpublish_product'):
            return ModeratorProductForm
        return ProductForm

    def get_success_url(self):
        return reverse('catalog:product_info', args=[self.kwargs.get('pk')])

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    raise_exception = True

    def get_queryset(self):
        # Владелец может удалять только свои товары, обладатель права can_delete_product - все
        if self.request.user.has_perm('catalog.can_delete_product'):
            return Product.objects.all()
        return Product.objects.filter(owner=self.request.user)

    def get_success_url(self):
        return reverse_lazy('catalog:catalog')

class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product
