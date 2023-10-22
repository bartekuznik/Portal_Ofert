from django.shortcuts import render
from .models import *
# Create your views here.

def list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'portal/list.html', context)