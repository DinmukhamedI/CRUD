from .models import Story, Exists
from django.forms import  ModelForm, TextInput, DateTimeInput, NumberInput

class StoryForm(ModelForm):
    class Meta:
        model = Story
        fields = ['username', 'email', 'product', 'date']

        widgets = {
            "username": TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            "email": TextInput(attrs={'class': 'form-control', 'placeholder': 'Email address'}),
            "product": TextInput(attrs={'class': 'form-control', 'placeholder': 'Product'}),
            "date": DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Date of buying'})
        }


class ExistsForm(ModelForm):
    class Meta:
        model = Exists
        fields = ['name', 'price', 'company']

        widgets = {
            "name": TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of product'}),
            "price": NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
            "company": TextInput(attrs={'class': 'form-control', 'placeholder': 'Company'})
        }
