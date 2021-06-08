from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import *
from .forms import ContactForm
# Create your views here.


def HomeView(request):
    about = About.objects.first()
    skills = Skill.objects.all()
    services = Service.objects.all()
    galleries = Gallery.objects.all().order_by('-id')

    contact = ContactForm()
    if request.method == 'POST':
        contact = ContactForm(request.POST)
        if contact.is_valid():
            contact.save()
        return redirect('/')

    konteks = {
        'title': 'Artso | Web Developer',
        'about': about,
        'skills': skills,
        'services': services,
        'galleries': galleries,
        'contact': contact,

    }
    return render(request, 'index.html', konteks)
