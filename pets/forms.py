from django import forms
from .models import Pet


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='Username',max_length=32, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    password = forms.CharField(required=True, label='Password', max_length=32, widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['pet', 'name', 'birthday']
        widgets = {
            'pet': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD'}),
        }
