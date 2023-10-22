from django.urls import path
from . import views

app_name = 'portal'

urlpatterns = [
    path('', views.offer_list, name='offer_list'),
]