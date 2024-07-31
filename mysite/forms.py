from django import forms
from .models import Comment, MainContent, Product

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class MainContentForm(forms.ModelForm):
    class Meta:
        model = MainContent
        fields = ['title', 'content', 'image']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'image']
