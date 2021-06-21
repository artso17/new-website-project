"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from home.views import *

urlpatterns = [
    path('delete-contact/<str:pk>/', DeleteContactView, name='deleteContact'),
    path('update-contact/<str:pk>/', UpdateContactView, name='updateContact'),
    path('delete-service/<str:pk>/', DeleteServiceView, name='deleteService'),
    path('update-service/<str:pk>/', UpdateServiceView, name='updateService'),
    path('create-service/', CreateServiceView, name="createService"),
    path('delete-gallery/<str:pk>/', DeleteGalleryView, name='deleteGallery'),
    path('update-gallery/<str:pk>/', UpdateGalleryView, name='updateGallery'),
    path('create-gallery', CreateGalleryView, name='createGallery'),
    path('delete-skill/<str:pk>/', DeleteSkillView, name='deleteSkill'),
    path('update-skill/<str:pk>/', UpdateSkillView, name='updateSkill'),
    path('create-skill/', CreateSkillView, name='createSkill'),
    path('delete-about/<str:pk>/', DeleteAboutView, name='deleteAbout'),
    path('update-about/<str:pk>/', UpdateAboutView, name='updateAbout'),
    path('create-about/', CreateAboutView, name='createAbout'),
    path('logout-user/', LogoutView, name='logout'),
    path('login-user/', LoginView, name='login'),
    # path('create-user/', CreateUserView, name='createUser'),
    path('mail-confirm/', MailConfirmView, name='mailConfirm'),
    path('list-view/', ListView, name='list'),
    path('', HomeView, name='home'),
    path('admin/', admin.site.urls),
    # path('ckeditor/', include('ckeditor_uploader.urls'))
    re_path(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT})
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
