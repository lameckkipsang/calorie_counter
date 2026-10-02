from django import forms
from .models import FoodItem

class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ['name', 'calories']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded focus:outline-none focus:border-blue-500',
                'placeholder': 'e.g., Apple'
            }),
            'calories': forms.NumberInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded focus:outline-none focus:border-blue-500',
                'placeholder': 'e.g., 95',
                'min': '0'
            }),
        }