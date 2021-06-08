from django import forms
from .models import *
from django_svg_image_form_field import SvgAndImageFormField


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        exclude = []
        field_classes = {
            'Image': SvgAndImageFormField,
        }


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        exclude = []
        field_classes = {
            'Image': SvgAndImageFormField,
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
