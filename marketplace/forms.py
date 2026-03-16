from django import forms
from .models import Service


class ServiceForm(forms.ModelForm):
    """
    Form for creating and updating service listings.
    """
    class Meta:
        model = Service
        fields = ['title', 'description', 'category', 'price', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'price': forms.NumberInput(attrs={'step': '0.01'}),
        }