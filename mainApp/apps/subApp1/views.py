from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *

import datetime

def index(request):
    print '*'*20+" index "+'*'*20
    return render(request, "subApp1/index.html")

def dashboard(request):
    print '*'*20+" dashboard "+'*'*20
    if 'key' not in request.session:
        return redirect('/')
    ### Get All Users
    c11=Person.objects.all()
    context = {
        "allPersons" : c11
    }
    return render(request, "subApp1/dashboard.html", context)

def user(request):
    print '*'*20+" user "+'*'*20
    if 'key' not in request.session:
        return redirect('/')
    return render(request, "subApp1/user.html")

def addUser(request):
    print '*'*20+" addUser "+'*'*20
    if 'key' not in request.session:
        return redirect('/')
    if request.method == "POST":
        ### Input Validation
        errors = Person.objects.person_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/user')
        else:
            ### Check Email Duplication
            c21=Person.objects.filter(email=request.POST.get('inputEmail'))
            if len(c21) > 0:
                errors["2error1"] = "This email address is in our system. Try again!"
                for tag, error in errors.iteritems():
                    messages.error(request, error, extra_tags=tag)
                return redirect('/user')
            ### Check Campus ID Duplication
            c22=Person.objects.filter(campusID=request.POST.get('inputCampusID'))
            if len(c21) > 0:
                errors["2error2"] = "This campus ID is in our system. Try again!"
                for tag, error in errors.iteritems():
                    messages.error(request, error, extra_tags=tag)
                return redirect('/user')
            ### Insert Into Database
            Person.objects.create(
                campusID=request.POST.get('inputCampusID'), 
                lastName=request.POST.get('inputLastName'),
                firstName=request.POST.get('inputFirstName'),
                dateBirth=request.POST.get('inputDateBirth'),
                address=request.POST.get('inputAddress'),
                phone=request.POST.get('inputPhone'),
                extNum=request.POST.get('inputExtNum'),
                email=request.POST.get('inputEmail'), 
                password=request.POST.get('inputPassword1'),
            )
    return redirect('/dashboard')

def system(request):
    print '*'*20+" system "+'*'*20
    if 'key' not in request.session:
        return redirect('/')
    ### Get All CatalogType
    c41=CatalogType.objects.all()
    context = {
        "allCatalogType" : c41
    }
    return render(request, "subApp1/system.html", context)

def addCatalogType(request):
    print '*'*20+" addCatalogType "+'*'*20
    if 'key' not in request.session:
        return redirect('/')
    if request.method == "POST":
        ### Input Validation
        errors = CatalogType.objects.person_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/system')
        else:
            ### Insert Into Database
            CatalogType.objects.create(
                name=request.POST.get('inputCatalogName'), 
            )
    return redirect('/system')

def login(request):
    print '*'*20+" login "+'*'*20
    # if 'key' not in request.session:
    #     return redirect('/')
    temp_e = request.POST.get('inputEmail')
    temp_p = request.POST.get('inputPassword')
    if request.method == "POST":
        errors = Person.objects.login_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/')
        else:
            c31 = Person.objects.filter(email=temp_e)
            if len(c31) > 0:
                c32 = Person.objects.get(email=temp_e)
                if c32.password != temp_p:
                    errors["3error1"] = "Invalid credentials. Try again!"
            else:
                errors["3error2"] = "Invalid credentials."
            if len(errors):
                for tag, error in errors.iteritems():
                    messages.error(request, error, extra_tags=tag)
                return redirect('/')
            else:
                request.session['key']  = temp_e
                return redirect('/dashboard')
    return redirect('/')

def logout(request):
    print '*'*20+" logout "+'*'*20
    if 'key' not in request.session:
        return redirect('/')
    request.session.flush()
    return redirect('/')