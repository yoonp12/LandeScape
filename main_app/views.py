from django.shortcuts import render, redirect
from django.contrib import messages
from main_app.models import *
import requests
import bcrypt


def index(request):
    return render(request, "valid/index.html")

# ======================================
# About, Blog
# ======================================

def about(request):

    return render(request, 'about.html')

def blog(request):

    return render(request, 'blog.html')

# ======================================
# Register, Login, and Logout
# ======================================

def register(request):
    if request.POST:
        errors = User.objects.reg_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')


        else:

            user = User.objects.create(
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],
                password=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            )
            request.session['user_id'] = user.id
            return redirect('/dashboard')

def login(request):
    if request.POST:
        errors = User.objects.log_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')

        else:
            user = User.objects.get(email=request.POST['email_input'])
            request.session['user_id'] = user.id
            return redirect('/dashboard')


def logout(request):
    request.session.clear()
    return redirect('/')

# ======================================
# Dashboard
# ======================================

def dashboard(request):
    if 'user_id' not in request.session:
        errors = User.objects.not_logged_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
    else:
        user_id = request.session['user_id']
        user = User.objects.get(id=user_id)
        context = {
            'user' : user
        }
        return render(request, 'home.html', context)

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