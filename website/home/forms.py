from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *
from django_svg_image_form_field import SvgAndImageFormField


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username',  'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.TextInput(attrs={'class': 'form-control'}),
        }


class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        exclude = []
        field = '__all__'
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Date_of_Birth': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'Address': forms.TextInput(attrs={'class': 'form-control'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control'}),
            'Phone': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        exclude = []
        field = '__all__'
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Skill_Range': forms.NumberInput(attrs={'class': 'form-control'}),
            'Publish': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        exclude = []
        fields = '__all__'
        field_classes = {
            'Image': SvgAndImageFormField,
        }


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        exclude = []
        fields = '__all__'
        field_classes = {
            'Image': SvgAndImageFormField,
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
