from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode


from .models import *
from .forms import *
from .decorators import *
from django.conf import settings
# Create your views here.


@unauthorized_user
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


@unauthorized_user
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


@login_required(login_url='home')
def LogoutView(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

    konteks = {
        'title': 'Logout',
    }

    return render(request, 'logout.html', konteks)


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
            # print(request.POST)
            email_konteks = {
                'name': request.POST['Name'],
                'email': request.POST['Email'],
                'subject': request.POST['Subject'],
                'body': request.POST['Message'],
            }
            # print(email_konteks)
            email_customer_body = render_to_string(
                'customer_email.html', email_konteks)
            email1 = EmailMessage(subject='Congratulations! Your Message was successfully sent',
                                  body=email_customer_body,
                                  from_email=settings.EMAIL_HOST_USER,
                                  to=[request.POST['Email']],
                                  )

            email_admin_body = render_to_string(
                'admin_email.html', email_konteks)
            email_admin = EmailMessage(subject='Customer Request',
                                       body=email_admin_body,
                                       from_email=settings.EMAIL_HOST_USER,
                                       to=[settings.EMAIL_HOST_USER],
                                       )
            email1.content_subtype = 'html'
            email_admin.content_subtype = 'html'
            email1.send()
            email_admin.send()
            return redirect('mailConfirm')

    konteks = {
        'title': 'Artso | Web Developer',
        'about': about,
        'skills': skills,
        'services': services,
        'galleries': galleries,
        'contact': contact,

    }
    return render(request, 'index.html', konteks)


def MailConfirmView(request):
    return render(request, 'mail_confirm.html')


@ login_required(login_url='home')
@ allowed_user(allowed_user=['admin'])
def ListView(request):
    abouts = About.objects.all()
    skills = Skill.objects.all()
    services = Service.objects.all()
    galleries = Gallery.objects.all().order_by('-id')
    contact = Contact.objects.all()

    konteks = {
        'title': 'List of Data Base',
        'abouts': abouts,
        'skills': skills,
        'services': services,
        'galleries': galleries,
        'contact': contact,
    }
    return render(request, 'list_view.html', konteks)


@ login_required(login_url='home')
@ allowed_user(allowed_user=['admin'])
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


@ login_required(login_url='home')
@ allowed_user(allowed_user=['admin'])
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


@ login_required(login_url='home')
@ allowed_user(allowed_user=['admin'])
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


# skill
@ login_required(login_url='home')
@ allowed_user(allowed_user=['admin'])
def CreateSkillView(request):
    form = SkillForm()
    if request.method == 'POST':
        form = SkillForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect("list")
    konteks = {
        'title': 'Add New Skill',
        'form': form,
    }
    return render(request, 'create_form.html', konteks)


@ login_required(login_url='home')
@ allowed_user(allowed_user=['admin'])
def UpdateSkillView(request, pk):
    data = Skill.objects.get(id=pk)
    form = SkillForm(instance=data)
    if request.method == 'POST':
        form = SkillForm(request.POST or None, instance=data)
        if form.is_valid():
            form.save()
            return redirect('list')
    konteks = {
        'title': 'Skill',
        'form': form,
    }
    return render(request, 'update_form.html', konteks)


@ login_required(login_url='home')
@ allowed_user(allowed_user=['admin'])
def DeleteSkillView(request, pk):
    form = Skill.objects.get(id=pk)
    konteks = {
        'title': 'Delete Data',
        'form': form,
    }
    if request.method == "POST":
        form.delete()
        return redirect('list')
    return render(request, 'delete_form.html', konteks)


# service
@ login_required(login_url='home')
@ allowed_user(allowed_user=['admin'])
def CreateServiceView(request):
    form = ServiceForm()
    if request.method == 'POST':
        form = ServiceForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect("list")
    konteks = {
        'title': 'Add New Service',
        'form': form,
    }
    return render(request, 'create_form.html', konteks)


@ login_required(login_url='home')
@ allowed_user(allowed_user=['admin'])
def UpdateServiceView(request, pk):
    data = Service.objects.get(id=pk)
    form = ServiceForm(instance=data)
    if request.method == 'POST':
        form = ServiceForm(request.POST or None, instance=data)
        if form.is_valid():
            form.save()
            return redirect('list')
    konteks = {
        'title': 'Service',
        'form': form,
    }
    return render(request, 'update_form.html', konteks)


@ login_required(login_url='home')
@ allowed_user(allowed_user=['admin'])
def DeleteServiceView(request, pk):
    form = Service.objects.get(id=pk)
    konteks = {
        'title': 'Delete Data',
        'form': form,
    }
    if request.method == "POST":
        form.delete()
        return redirect('list')
    return render(request, 'delete_form.html', konteks)


# gallery
@ login_required(login_url='home')
@ allowed_user(allowed_user=['admin'])
def CreateGalleryView(request):
    form = GalleryForm()
    if request.method == 'POST':
        form = GalleryForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect("list")
    konteks = {
        'title': 'Add New Gallery',
        'form': form,
    }
    return render(request, 'create_form.html', konteks)


@ login_required(login_url='home')
@ allowed_user(allowed_user=['admin'])
def UpdateGalleryView(request, pk):
    data = Gallery.objects.get(id=pk)
    form = GalleryForm(instance=data)
    if request.method == 'POST':
        form = GalleryForm(request.POST or None, instance=data)
        if form.is_valid():
            form.save()
            return redirect('list')
    konteks = {
        'title': 'Gallery',
        'form': form,
    }
    return render(request, 'update_form.html', konteks)


@ login_required(login_url='home')
@ allowed_user(allowed_user=['admin'])
def DeleteGalleryView(request, pk):
    form = Gallery.objects.get(id=pk)
    konteks = {
        'title': 'Delete Data',
        'form': form,
    }
    if request.method == "POST":
        form.delete()
        return redirect('list')
    return render(request, 'delete_form.html', konteks)


# contact
@ login_required(login_url='home')
@ allowed_user(allowed_user=['admin'])
def UpdateContactView(request, pk):
    data = Contact.objects.get(id=pk)
    form = ContactForm(instance=data)
    if request.method == 'POST':
        form = ContactForm(request.POST or None, instance=data)
        if form.is_valid():
            form.save()
            return redirect('list')
    konteks = {
        'title': 'Contact',
        'form': form,
    }
    return render(request, 'update_form.html', konteks)


@ login_required(login_url='home')
@ allowed_user(allowed_user=['admin'])
def DeleteContactView(request, pk):
    form = Contact.objects.get(id=pk)
    konteks = {
        'title': 'Delete Data',
        'form': form,
    }
    if request.method == "POST":
        form.delete()
        return redirect('list')
    return render(request, 'delete_form.html', konteks)
