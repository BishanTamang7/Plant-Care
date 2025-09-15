from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User

class UserRegistrationForm(forms.ModelForm):
    ROLE_CHOICES = (
        ("visitor", "Visitor"),
        ("nursery", "Nursery"),
    )

    role = forms.ChoiceField(
        choices=ROLE_CHOICES,
        widget=forms.RadioSelect(attrs={"class": "hidden"})
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "w-full px-4 py-3 border border-gray-300 rounded-lg "
                     "focus:ring focus:ring-green-200 outline-none"
        })
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "w-full px-4 py-3 border border-gray-300 rounded-lg "
                     "focus:ring focus:ring-green-200 outline-none"
        })
    )

    class Meta:
        model = User
        fields = [
            "role", "username", "email",
            "nursery_name", "nursery_address",
            "phone_number", "nursery_description"
        ]
        widgets = {
            "username": forms.TextInput(attrs={
                "class": "w-full px-4 py-3 border border-gray-300 rounded-lg "
                         "focus:ring focus:ring-green-200 outline-none"
            }),
            "email": forms.EmailInput(attrs={
                "class": "w-full px-4 py-3 border border-gray-300 rounded-lg "
                         "focus:ring focus:ring-green-200 outline-none"
            }),
            "nursery_name": forms.TextInput(attrs={
                "class": "w-full px-4 py-3 border border-gray-300 rounded-lg "
                         "focus:ring focus:ring-green-200 outline-none"
            }),
            "nursery_address": forms.Textarea(attrs={
                "class": "w-full px-4 py-3 border border-gray-300 rounded-lg "
                         "focus:ring focus:ring-green-200 outline-none",
                "rows": 2
            }),
            "phone_number": forms.TextInput(attrs={
                "class": "w-full px-4 py-3 border border-gray-300 rounded-lg "
                         "focus:ring focus:ring-green-200 outline-none"
            }),
            "nursery_description": forms.Textarea(attrs={
                "class": "w-full px-4 py-3 border border-gray-300 rounded-lg "
                         "focus:ring focus:ring-green-200 outline-none",
                "rows": 3
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("password") != cleaned_data.get("confirm_password"):
            raise forms.ValidationError("Passwords do not match")

        role = cleaned_data.get("role")
        if role == "visitor":
            # clear nursery fields if visitor
            for f in ["nursery_name", "nursery_address", "phone_number", "nursery_description"]:
                cleaned_data[f] = None
        elif role == "nursery":
            if not cleaned_data.get("nursery_name"):
                raise forms.ValidationError("Nursery name is required for nursery registration")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = self.cleaned_data["role"]
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            "id": "id_username",
            "class": "w-full px-4 py-3 border border-gray-300 rounded-lg outline-none transition-colors bg-gray-50",
            "placeholder": "Enter your email",
        })
    )
    
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            "id": "id_password",
            "class": "w-full px-4 py-3 border border-gray-300 rounded-lg outline-none transition-colors bg-gray-50",
            "placeholder": "Enter your password",
        })
    )