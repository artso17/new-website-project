from django.contrib import admin

# Register your models here.
from .models import *
from .forms import *


class ReadOnly(admin.ModelAdmin):
    readonly_fields = ['slug']


class ServiceAdmin(admin.ModelAdmin):
    form = ServiceForm
    readonly_fields = ['slug']


class GalleryAdmin(admin.ModelAdmin):
    form = GalleryForm
    readonly_fields = ['slug']


class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ['Created']


admin.site.register(About)
admin.site.register(Skill, ReadOnly)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Contact, ContactAdmin)
