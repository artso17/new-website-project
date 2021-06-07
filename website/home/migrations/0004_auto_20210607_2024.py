# Generated by Django 3.0 on 2021-06-07 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210607_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='Height',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='Image',
            field=models.ImageField(height_field='Height', upload_to='image/gallery', width_field='Width'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='Width',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='Image',
            field=models.ImageField(height_field='Height', upload_to='image/service', width_field='Width'),
        ),
    ]