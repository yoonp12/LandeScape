from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('register_page', views.register_page),
    path('register', views.register),
    path('login_page', views.login_page),
    path('login', views.login),
    path('logout', views.logout),
    path('profile', views.profile),
    path('about', views.about),
    path('blog', views.blog),
    path('map', views.my_map),
    path('trail/<int:id>', views.trail),
    path('favorite/<int:id>', views.favorite),
    path('completed/<int:id>', views.completed),
    path('Cremove/<int:id>', views.Cremove),
    path('Fremove/<int:id>', views.Fremove),
]

