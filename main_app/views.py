from django.shortcuts import render, redirect
from django.contrib import messages
from main_app.models import *
import requests
import bcrypt


def index(request):
    return render(request, "valid/extra.html")

def my_map(request):
    return render(request, "valid/map.html")

def trail(request, id):
    url = "https://www.hikingproject.com/data/get-trails-by-id?ids="+ str(id) +"&key=200692212-0c29a6ccde17f1eeb5873b8087e497d2"
    r = requests.get(url)
    data = r.json() 
    print(data['trails'][0])

    context = {
        'data' : data['trails'][0],
    }
    return render(request, "valid/trail.html", context)