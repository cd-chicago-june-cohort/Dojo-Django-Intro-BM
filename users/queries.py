import django
from django.db.models import Count

from apps.user_login.models import *


def everyone():
    everyone = User.objects.all()
    for them in everyone:
        print them.first_name, them.last_name

def first():
    first = User.objects.first()
    print first.first_name, first.last_name

def last():
    last = User.objects.last()
    print last.first_name, last.last_name

def usefirst():
    usefirst = User.objects.all().order_by('-first_name')
    for user in usefirst:
        print user.first_name, user.last_name

def balds():
    balds = User.objects.filter(first_name="Bald")
    for bald in balds:
        print bald.first_name, bald.last_name

def switch_last_name(id_int, newlastname):
    user = User.objects.get(id=id_int)
    print user.first_name, user.last_name
    print "is now"
    user.last_name = newlastname
    print user.first_name, user.last_name

def delete_record(id_int):
    user = User.objects.get(id=id_int).delete()
    print "Finished."




