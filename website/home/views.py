from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm


from .models import *
from .forms import *
# Create your views here.


def CreateUserView(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data('username')
            messages.success(
                request, f'The Account for {user} was created successfully')
        return redirect('login')

    konteks = {
        'title': 'registration',
        'form': form,
    }
    return render(request, 'create_user.html', konteks)


def LoginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list')

    konteks = {
        'title': 'Login',
    }
    return render(request, 'login.html', konteks)


@login_required(login_url='login')
def LogoutView(request):
    logout(request)
    return redirect('login')


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


@login_required(login_url='login')
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


@login_required(login_url='login')
def CreateAboutView(request):
    form = AboutForm()
    if request.method == 'POST':
        form = AboutForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect("list")
    konteks = {
        'title': 'Add New About',
        'form': form,
    }
    return render(request, 'create_form.html', konteks)


@login_required(login_url='login')
def UpdateAboutView(request, pk):
    data = About.objects.get(id=pk)
    form = AboutForm(instance=data)
    if request.method == 'POST':
        form = AboutForm(request.POST or None, instance=data)
        if form.is_valid():
            form.save()
        return redirect('list')
    konteks = {
        'title': 'About',
        'form': form,
    }
    return render(request, 'update_form.html', konteks)


@login_required(login_url='login')
def DeleteAboutView(request, pk):
    form = About.objects.get(id=pk)
    konteks = {
        'title': 'Delete Data',
        'form': form,
    }
    if request.method == "POST":
        form.delete()
        return redirect('list')
    return render(request, 'delete_form.html', konteks)
