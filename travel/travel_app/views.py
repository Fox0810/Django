from django.shortcuts import render, redirect
from django.http import HttpResponse
from travel_app.models import Category, Article, Load, City, Tour
from travel_app.forms import ArticleForm
##
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic.base import View


# Create your views here.
def get_item_all(request):
    menu = data = Category.objects.all()
    data =Article.objects.all()
    return render(request, 'travel_app/get_item_all.html',{'data': data, 'menu': menu})


def get_my_items(request):
    menu = Category.objects.all()
    data = Article.objects.filter(user=request.user)
    category = {'short_name': 'My articles', 'about':'You can edit or remote it'}
    return render(request, 'travel_app/get_item_category.html', {'data': data, 'category': category, 'menu': menu})


def get_item_one(request, id):
    menu = Category.objects.all()
    data = Article.objects.get(id=id)
    return render(request, 'travel_app/get_item_one.html', {'data': data, 'menu': menu})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "travel_app/login.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/"
    template_name = "travel_app/registration.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


def add_item(request):
    menu = Category.objects.all()
    form = ArticleForm()
    msg = ''
    if request.method == 'POST':
        category = Category.objects.get(id=request.POST['category'])
        article = Article.objects.create(text=request.POST['text'], title=request.POST['title'],
                                         summary=request.POST['summary'], category=category,
                                         user=request.user)
        article.save()
        msg = 'ok'

    return render(request, 'travel_app/add_item.html', {'form': form, 'menu': menu, 'msg': msg})

def update_item(request, id):
    menu = Category.objects.all()
    obj = Article.objects.get(id=id)
    form = ArticleForm(instance=obj)

    if request.method == 'POST':
        category = Category.objects.get(id=request.POST['category'])
        Article.objects.filter(id=id).update(text=request.POST['text'],title=request.POST['title'],
                                         summary=request.POST['summary'], category=category, edit_count=+1)
        return redirect('get_item_one', id)

    return render(request, 'travel_app/update_item.html', {'form': form, 'menu': menu})

def delete_item(request, id):
    Article.objects.get(id=id).delete()
    return redirect('get_my_items')


def index(request):
    data = Category.objects.all()
    return render(request, 'travel_app/index.html', {'data': data})


def get_item_category(request, id):
    menu = Category.objects.all()
    data = Tour.objects.filter(category_id=id)
    category = Category.objects.get(pk=id)
    return render(request, 'travel_app/get_item_category.html', {'data': data, 'menu': menu, 'category': category})


def about(request):
    return render(request, 'travel_app/about.html')


def tour(request):
    menu = Category.objects.all()
    data = Load.objects.all()
    category = Tour.objects.all()
    city = City.objects.all()
    return render(request, 'travel_app/tour.html', {'data': data, 'menu': menu, 'category': category, 'city': city})


def load(request):
    menu = Category.objects.all()
    data = Load.objects.all()
    return render(request, 'travel_app/load.html', {'data': data, 'menu': menu})



def news(request):
    data = Article.objects.all()
    return render(request, 'travel_app/news.html', {'data': data})


def contacts(request):
    return render(request, 'travel_app/contacts.html')


def based_page3(request):
    data = dict()
    data['tel'] = 'Тел/факс: +37517 678 33 18'
    data['mts'] = 'MTC: +37533 567 89 45'
    data['a1'] = 'A1: +37529 567 89 45'
    data['life'] = 'Life: +37529 567 89 45'
    data['address'] = 'г. Минск, пр-т Победителей, 54 офис 18'
    return render(request, 'travel_app/get_item_all.html', {'data': data})
