from django.urls import path
from travel_app.views import index, about, contacts, news, load, get_item_category, tour, add_item,\
    RegisterFormView, LoginFormView, LogoutView, get_item_all, get_my_items, get_item_one, \
    update_item, delete_item
urlpatterns = [
    path('', index),
    path('index/', index, name='index'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('news/', news, name='news'),
    path('load/', load, name='load'),
    path('tour/', tour, name='tour'),

    path('category/<int:id>/', get_item_category, name='get_item_category'),
    path('article/<int:id>/', get_item_one, name='get_item_one'),
    path('myarticles/', get_my_items, name='get_my_items'),
    path('all/', get_item_all, name='get_item_all'),
    path('addarticle/', add_item, name='add_item'),
    path('editarticle/<int:id>/', update_item, name='update_item'),
    path('delarticles/<int:id>/', delete_item, name='delete_item'),


    path('registration/', RegisterFormView.as_view(), name='registration'),
    path('login/', LoginFormView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
