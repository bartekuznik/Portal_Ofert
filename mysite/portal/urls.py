from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from portal.views import ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = 'portal'

urlpatterns = [
    path('', views.list, name='list'),
    path('product/<int:pk>/', views.product_detail, name='product-detail'),
    path('login/', auth_views.LoginView.as_view(template_name='portal/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='portal/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('product/new/', ProductCreateView.as_view(), name='product-create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
    path('profile/update/', views.user_edit_profile, name='profile-update'),
    path('profile/', views.user_detail_view, name='profile-detail'),
]