# Generated by Django 3.0 on 2021-06-24 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_contact_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
