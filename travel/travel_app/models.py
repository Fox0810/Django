from django.db import models
import datetime


# Create your models here.
class Category(models.Model):
    short_name = models.CharField(max_length=20, db_index=True)

    def __str__(self):
        return self.short_name

class Tour(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=1000)
    text = models.TextField(max_length=2000)
    edit_count = models.IntegerField(default=0)
    image = models.ImageField(upload_to='travel_app/images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.title

class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False, blank=False)
    date = models.DateField(default=datetime.date.today)
    summary = models.CharField(max_length=200)
    text = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='travel_app/images', default='travel_app/images/default.jpg')
    user = models.ForeignKey('auth.User', default=1, on_delete=models.CASCADE, verbose_name='user')

    def __str__(self):
        return self.title

    @property
    def photo_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url


class Load(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False, blank=False)
    text = models.TextField(max_length=1000)
    edit_count = models.IntegerField(default=0)
    image = models.ImageField(upload_to='travel_app/images', blank=True)

    def __str__(self):
        return self.title


class City(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False, blank=False)
    text = models.TextField(max_length=500)
    edit_count = models.IntegerField(default=0)
    image = models.ImageField(upload_to='travel_app/images', blank=True)

    def __str__(self):
        return self.title

class Likemark(models.Model):
    article = models.ForeignKey(Article,  on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='user')
    mark = models.PositiveSmallIntegerField(default=5)

class Read(models.Model):
    state = models.BooleanField(default=True)

class List(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='user')
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    read = models.ForeignKey(Read, on_delete=models.CASCADE, null=True)
    count = models.PositiveSmallIntegerField(default=1)