from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'portal'

urlpatterns = [
    path('', views.list, name='list'),
    path('login/', auth_views.LoginView.as_view(template_name='portal/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='portal/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
]