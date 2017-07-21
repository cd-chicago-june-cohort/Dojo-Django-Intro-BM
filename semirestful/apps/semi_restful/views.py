from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import strftime, localtime
 
from models import *

def index(request):
    return redirect('/users')

def users(request):
    all_users = User.objects.all()
    context = {

        'all_users': all_users,
    
    }
    return render(request, 'semi_restful/index.html', context)

def newuser(request):
    return render(request, 'semi_restful/newuser.html')

def edituser(request, user_id):
    current_user = User.objects.filter(id=user_id)
    print current_user
    context = {

        'current_user': current_user,
    
    }
    return render(request, 'semi_restful/edituser.html', context)

def showuser(request, user_id):
    current_user = User.objects.filter(id=user_id)
    print current_user
    context = {

        'current_user': current_user,
    
    }
    return render(request, 'semi_restful/showuser.html', context)

def createuser(request):
    if request.method == 'POST':
        name=request.POST['first_name'] + ' ' + request.POST['last_name']
        email=request.POST['email']
        User.objects.create(name=name, email=email)
    return redirect('/')

def deleteuser(request, user_id):
    current_user = User.objects.get(id=user_id)
    current_user.delete()
    print "deleted"
    return redirect('/')

def finaledit(request, user_id):
    if request.method == 'POST':
        current_user = User.objects.get(id=user_id)
        current_user.email=request.POST['email']
        current_user.save()
    return redirect('/')
    



