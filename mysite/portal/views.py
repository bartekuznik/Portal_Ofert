from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def list(request):
    products = Product.objects.all()
    return render(request, 'portal/list.html', {'products': products})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            Profile.objects.create(user=new_user)
            return redirect('portal:login')
    else:
        form = UserCreationForm(request.POST)
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
    reviews = ProductRevirev.objects.filter(product__id = pk) # lub: (product = product)

    if request.method == 'POST':
        review_form = ProductReviewForm(request.POST)
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.user = request.user
            new_review.product = product
            new_review.save()
    else:
        review_form = ProductReviewForm(request.POST)

    return render(request, 'portal/detail.html', {'product': product, 'reviews':reviews, 'review_form':review_form})

@login_required
def user_detail_view(request):
    products = Product.objects.filter(author = request.user)
    return render(request, 'portal/profile_detail.html', {'products': products})

@login_required
def user_edit_profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,'portal/profile_detail_update.html', {'user_form': user_form,'profile_form': profile_form})