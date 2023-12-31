from django import forms
from django.contrib.auth.models import User
from .models import *


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')
        labels = {
            'username': 'Nazwa użytkownika',
            'email': 'Adres e-mail'
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('description', 'image')
        labels ={
            'description': 'Opis profilu',
            'image': 'Zdjęcie profilowe'
        }

class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductRevirev
        fields = ('description', 'reviev_choice')
        labels = {
            'description': 'Opinia o produkcie',
            'reviev_choice': 'Ocena produktu'
        }