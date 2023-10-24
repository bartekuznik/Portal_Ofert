from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['sub_category', 'name', 'image', 'description', 'price', 'quantity', 'available']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    template_name ='portal/product_update.html'
    fields = ['sub_category', 'name', 'image', 'description', 'price', 'quantity', 'available']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        product = self.get_object()
        if self.request.user == product.author:
            return True
        else:
            return False
        
class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url ='/'

    def test_func(self):
        product = self.get_object()
        if self.request.user == product.author:
            return True
        else:
            return False

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'portal/detail.html', {'product': product})