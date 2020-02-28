from django.shortcuts import render, redirect
from django.contrib import messages
from main_app.models import *
import requests
import bcrypt

# ======================================
# Dashboard
# ======================================

def home(request):
    return render(request, 'valid/home.html')

# ======================================
# Register, Login, and Logout
# ======================================
def register_page(request):
    return render(request, "valid/register_page.html")


def register(request):
    if request.POST:
        errors = User.objects.reg_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/register_page')


        else:

            user = User.objects.create(
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],
                password=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            )
            request.session['user_id'] = user.id
            return redirect('/profile')

def login_page(request):
    return render(request, "valid/login_page.html")

def login(request):
    if request.POST:
        errors = User.objects.log_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/login_page')

        else:
            user = User.objects.get(email=request.POST['email_input'])
            request.session['user_id'] = user.id
            return redirect('/profile')

def logout(request):
    request.session.clear()
    return redirect('/')

# ======================================
# Profile, Favorite, Completed 
# ======================================
def edit_profile(request):
    context = {
        "user" : User.objects.get(id = request.session['user_id'])
    }
    return render (request, "valid/edit_profile.html", context)

def change_profile(request):
    if request.POST:
        user = User.objects.get(id=request.session["user_id"])
        user.first_name = request.POST['first_name']
        user.save()
    if request.POST: 
        user = User.objects.get(id=request.session["user_id"])   
        user.last_name = request.POST['last_name']
        user.save()
    if request.POST:  
        user = User.objects.get(id=request.session["user_id"])  
        user.email = request.POST['email']
        user.save()
    # if request.POST:  
    #     user = User.objects.get(id=request.session["user_id"])  
    #     user.password = request.POST['password']
    #     user.save()
    if request.POST:  
        user = User.objects.get(id=request.session["user_id"])  
        user.hometown = request.POST['hometown']
        user.save()
    if request.POST:  
        user = User.objects.get(id=request.session["user_id"])  
        user.info = request.POST['bio']
        user.save()
    messages.success (request, "Profile was successfully updated!")
    return redirect("/profile")

def profile(request):
    if 'user_id' not in request.session:
        errors = User.objects.not_logged_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/register_page')
    
    favorites = favoriteTrail.objects.filter(user_id=request.session['user_id'])
    favorites_ids = []
    completed = completedTrail.objects.filter(user_id=request.session['user_id'])
    completed_ids = []
    for favorite in favorites:
        favorites_ids.append(str(favorite.trail_id))
    for completed in completed:
        completed_ids.append(str(completed.trail_id))
    
    Furl = "https://www.hikingproject.com/data/get-trails-by-id?ids="+ ",".join(favorites_ids) + "&key=200692212-0c29a6ccde17f1eeb5873b8087e497d2"
    Fr = requests.get(Furl)
    Fdata = Fr.json()

    Curl = "https://www.hikingproject.com/data/get-trails-by-id?ids="+ ",".join(completed_ids)+"&key=200692212-0c29a6ccde17f1eeb5873b8087e497d2"
    Cr = requests.get(Curl)
    Cdata = Cr.json() 
 
    context = {
        "user" : User.objects.get(id=request.session['user_id']),
        "Fdata" : Fdata['trails'],
        "Cdata" : Cdata['trails'],
    }
    return render(request, 'valid/profile.html', context)

def favorite(request, id):
    if 'user_id' not in request.session:
        errors = User.objects.not_logged_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/register_page')
    if 'user_id' in request.session:
        user = User.objects.get(id=request.session["user_id"])
        favorite = favoriteTrail.objects.create(trail_id=id, user=user)
        return redirect('/profile')
    else:
        return render(request, "valid/trail/"+ str(id))
def Fcompleted(request, id):
    if request.POST:
        user = User.objects.get(id=request.session["user_id"])
        completed = completedTrail.objects.create(trail_id=id, user=user)
        favorite = favoriteTrail.objects.get(trail_id=id, user=user)
        favorite.delete()
        return redirect('/profile')
    else:
        return render(request, "valid/trail/"+ str(id))

def completed(request, id):
    if request.POST:
        user = User.objects.get(id=request.session["user_id"])
        completed = completedTrail.objects.create(trail_id=id, user=user)
        return redirect('/profile')
    else:
        return render(request, "valid/trail/"+ str(id))

def Fremove(request,id):
    a = favoriteTrail.objects.get(trail_id=id)
    a.delete()
    return redirect("/profile")

def Cremove(request,id):
    b = completedTrail.objects.get(trail_id=id)
    b.delete()
    return redirect("/profile")


# ======================================
# My map, trail
# ======================================

def my_map(request):
    return render(request, "valid/map.html")

def trail(request, id):
    url = "https://www.hikingproject.com/data/get-trails-by-id?ids="+ str(id) +"&key=200692212-0c29a6ccde17f1eeb5873b8087e497d2"
    r = requests.get(url)
    data = r.json() 

    context = {
        'data' : data['trails'][0],
    }
    return render(request, "valid/trail.html", context)

# ======================================
# About, Blog
# ======================================

def about(request):

    return render(request, 'valid/about.html')

def blog(request):

    return render(request, 'valid/blog.html')

def login_main(request):

    return render(request, 'valid/login.html')








