from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'portal/list.html', context)

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            Profile.objects.create(user=new_user)
            return redirect('portal:login')
    else:
        form = UserCreationForm()
    return render(request, 'portal/register.html', {'form': form})