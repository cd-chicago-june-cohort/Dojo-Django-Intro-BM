from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from time import strftime, localtime

def index(request):

    return render(request, 'books_authors/index.html')