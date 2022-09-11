# Generated by Django 4.1 on 2022-09-09 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_app', '0005_alter_article_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default='travel_app/images/default.jpg', upload_to='travel_app/images'),
        ),
    ]