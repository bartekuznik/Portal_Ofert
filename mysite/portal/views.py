from django.shortcuts import render
from .models import *
# Create your views here.

def offer_list(request):
    products = Product.objects.all()
    return render(request, 'portal/list.html', {'products': products})