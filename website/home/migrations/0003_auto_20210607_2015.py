# Generated by Django 3.0 on 2021-06-07 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210607_1753'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='Slug',
            new_name='slug',
        ),
        migrations.AddField(
            model_name='gallery',
            name='Is_Published',
            field=models.BooleanField(default=False),
        ),
    ]
