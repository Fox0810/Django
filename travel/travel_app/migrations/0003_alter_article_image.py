# Generated by Django 4.1 on 2022-09-09 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_app', '0002_read_list_likemark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default='travel_app/images/', upload_to='travel_app/images/'),
        ),
    ]