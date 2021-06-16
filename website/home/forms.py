from django import forms
from .models import *
from django_svg_image_form_field import SvgAndImageFormField


class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        exclude = []
        field = '__all__'


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        exclude = []
        field = '__all__'


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
