from django import forms
from .models import Category


class CategoryForm(forms.ModelForm):
    model = Category
    fields = ['category_name', 'description']