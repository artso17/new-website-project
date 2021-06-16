from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import *
from .forms import *
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


def ListView(request):
    abouts = About.objects.all()
    skills = Skill.objects.all()
    services = Service.objects.all()
    galleries = Gallery.objects.all().order_by('-id')
    contact = Contact.objects.all()

    konteks = {
        'title': 'List Data Base',
        'abouts': abouts,
        'skills': skills,
        'services': services,
        'galleries': galleries,
        'contact': contact,
    }
    return render(request, 'list_view.html', konteks)


def CreateAboutView(request):
    about = AboutForm()
    if request.method == 'POST':
        about = AboutForm(request.POST)
        if about.is_valid():
            about.save()
        return redirect('list-view')
    konteks = {
        'title': 'Add New About',
        'about': about,
    }
    return render(request, 'create_about.html', konteks)
