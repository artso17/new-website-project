# Generated by Django 3.0 on 2021-06-16 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20210613_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='Skill',
            field=models.ManyToManyField(blank=True, to='home.Skill'),
        ),
    ]
