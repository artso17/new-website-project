from django.db import models
from django.utils.text import slugify
# from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class About(models.Model):
    Name = models.CharField(max_length=100)
    Date_of_Birth = models.DateField()
    Address = models.CharField(max_length=200)
    Email = models.EmailField()
    Phone = models.CharField(max_length=20)
    Image = models.ImageField(upload_to='image/about', null=True)

    def __str__(self):
        return '{}.{}'.format(self.id, self.Name)


class Skill(models.Model):
    Name = models.CharField(max_length=100)
    Skill_Range = models.PositiveSmallIntegerField()
    Publish = models.BooleanField(default=False)
    slug = models.SlugField(editable=False, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.Name)

    def save(self):
        self.slug = slugify(self.Name)
        super(Skill, self).save()


class Service(models.Model):
    Name = models.CharField(max_length=100)
    Image = models.ImageField(
        upload_to='image/service', height_field='Height', width_field='Width')
    Height = models.IntegerField(default=0, null=True, blank=True)
    Width = models.IntegerField(default=0, null=True, blank=True)
    Body = models.TextField()
    Publish = models.BooleanField(default=False)
    slug = models.SlugField(editable=False, blank=True, null=True)

    def __str__(self):
        return '{}.{}'.format(self.id, self.Name)

    def save(self):
        self.slug = slugify(self.Name)
        super(Service, self).save()


class Gallery(models.Model):
    Name = models.CharField(max_length=100)
    Skill = models.ManyToManyField(
        Skill,  blank=True)
    Image = models.ImageField(
        upload_to='image/gallery', height_field='Height', width_field='Width')
    Height = models.IntegerField(default=0, null=True, blank=True)
    Width = models.IntegerField(default=0, null=True, blank=True)
    slug = models.SlugField(blank=True, null=True, editable=False)
    Publish = models.BooleanField(default=False)

    def __str__(self):
        return '{}.{}'.format(self.id, self.Name)

    def save(self):
        self.slug = slugify(self.Name)
        super(Gallery, self).save()


class Contact(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Subject = models.CharField(max_length=100)
    Message = models.TextField()
    Readed = models.BooleanField(default=False)
    Created = models.DateTimeField(
        auto_now_add=True, blank=True, editable=False)
    Updated = models.DateTimeField(
        auto_now=True, blank=True, editable=False)

    def __str__(self):
        return str(self.Name)
