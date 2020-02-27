from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('dashboard', views.dashboard),
    path('about', views.about),
    path('blog', views.blog),
    path('map', views.my_map),
    path('trail/<int:id>', views.trail),
]
