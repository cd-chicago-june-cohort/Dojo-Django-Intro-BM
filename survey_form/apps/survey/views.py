# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from time import strftime, localtime

def index(request):

    return render(request, 'survey/index.html')

def result(request):

    if request.method == 'POST':
        print request.POST

    if 'counter' not in request.session:
        request.session['counter']=0    

    request.session['name']=request.POST['name']
    request.session['dojo']=request.POST['dojo']
    request.session['language']=request.POST['language']
    request.session['comments']=request.POST['comments']
    request.session['counter'] += 1
    request.session['resend']=request.session['counter']+1

    context = {

    'name': request.session['name'],
    'dojo': request.session['dojo'],
    'language': request.session['language']

    }

    return render(request, 'survey/result.html', context)

def reset(request):

    request.session.flush()
    return redirect('/')