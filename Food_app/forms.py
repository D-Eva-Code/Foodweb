from django import forms
from.models import Item

class Itemform(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['Item_name','Item_description','Item_price', 'Item_image']
        widgets = {
            'Item_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter item name', 'style': 'width:50%;'}),
            'Item_description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter item description', 'style': 'width:50%;'}),
            'Item_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter item price','style': 'width:50%;'}),
            'Item_image': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter item image URL', 'style': 'width:50%;'}),
        }