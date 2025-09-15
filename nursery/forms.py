from django import forms
from .models import Plant
from account.models import User

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['name', 'category', 'price', 'image', 'care_instructions', 'care_level']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full border rounded-lg px-3 py-2',
                'placeholder': 'Enter plant name'
            }),
            'category': forms.Select(attrs={
                'class': 'w-full border rounded-lg px-3 py-2',
            }),
            'price': forms.NumberInput(attrs={
                'class': 'w-full border rounded-lg px-3 py-2',
                'placeholder': 'Enter price in NPR'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'w-full border rounded-lg px-3 py-2',
            }),
            'care_instructions': forms.Textarea(attrs={
                'class': 'w-full border rounded-lg px-3 py-2 h-32',
                'placeholder': 'Write care instructions...'
            }),
            'care_level': forms.Select(attrs={
                'class': 'w-full border rounded-lg px-3 py-2',
            }),
        }


class NurseryProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "nursery_name",
            "email",
            "nursery_address",
            "phone_number",
            "nursery_description",
        ]
        widgets = {
            "nursery_name": forms.TextInput(attrs={"class": "input"}),
            "email": forms.EmailInput(attrs={"class": "input"}),
            "nursery_address": forms.Textarea(attrs={"class": "input", "rows": 3}),
            "phone_number": forms.TextInput(attrs={"class": "input"}),
            "nursery_description": forms.Textarea(attrs={"class": "input", "rows": 4}),
        }