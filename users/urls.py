from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users.apps import UsersConfig
from .views import UserCreateView, UserUpdateView, UserDetailView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='catalog:catalog'), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('users/<str:email>', UserDetailView.as_view(), name='user_info'),
    path('users/<str:email>/update', UserUpdateView.as_view(), name='user_update')
]