from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from time import strftime, localtime

def index(request):
    if 'new_word' not in request.session:
        request.session['new_word']=[]

    return render(request, 'session_words/index.html')



def newword(request):

    if request.method == 'POST':
        print request.POST

    request.session['font']='big'

    if 'font' not in request.POST:
        request.session['font']='reg'
        print request.session['font']
    
    word_data = request.session['new_word']
    word_data.append({
        'word': request.POST['newword'],
        'color': request.POST['color'],
        'font': request.session['font'],
        'time': strftime("%c", localtime())
    })

    return redirect('/')



def reset(request):

    request.session.flush()
    return redirect('/')