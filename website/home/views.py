from django.shortcuts import render
from .models import *

# Create your views here.


def HomeView(request):
    about = About.objects.first()
    skills = Skill.objects.all()
    services = Service.objects.all()
    galleries = Gallery.objects.all()
    konteks = {
        'about': about,
        'skills': skills,
        'services': services,
        'galleries': galleries,

    }
    return render(request, 'index.html', konteks)
