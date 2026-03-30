from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import Article


# Create your views here.
class ArticleListView(ListView):
    model = Article

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_published=True)

class ArticleCreateView(CreateView):
    model = Article
    fields = ['title', 'body', 'preview']
    template_name = 'blog/article_form.html'
    success_url = reverse_lazy('blog:blog')

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'
    context_object_name = 'article'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['title', 'body', 'preview']
    template_name = 'blog/article_form.html'
    success_url = reverse_lazy('blog:blog')

    def get_success_url(self):
        return reverse('blog:article_info', args=[self.kwargs.get('pk')])

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'blog/article_confirm_delete.html'
    success_url = reverse_lazy('article_detail')