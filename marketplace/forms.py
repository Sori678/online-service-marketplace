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
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }