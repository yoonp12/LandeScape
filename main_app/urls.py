from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login_main', views.login_main),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('profile', views.profile),
    path('about', views.about),
    path('blog', views.blog),
    path('map', views.my_map),
    path('trail/<int:id>', views.trail),
    path('favorite/<int:id>', views.favorite),
    path('completed/<int:id>', views.completed),
]

