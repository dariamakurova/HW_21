import secrets

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login

from config.settings import EMAIL_HOST_USER
from .forms import UserRegisterForm, UserForm
from .models import User


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать в наш сервис'
        message = 'Спасибо, что зарегистрировались в нашем сервисе!'
        from_email = 'dariamak.python@yandex.ru'
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)

class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('catalog:catalog')
    slug_field = 'email'
    slug_url_kwarg = 'email'

class UserDetailView(DetailView):
    model = User
    slug_field = 'email'
    slug_url_kwarg = 'email'