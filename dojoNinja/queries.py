import django
from django.db.models import Count
 
from apps.dojo_ninjas.models import *

def create_dojo(name, city, state):
    return Dojos.objects.create(name=name, city=city, state=state)

def delete_dojo(name):
    Dojos.objects.get(name=name).delete()


def create_ninja(dojo_name, first_name, last_name):
    dojo = Dojos.objects.get(name=dojo_name)
    return Ninjas.objects.create(dojo=dojo, first_name=first_name, last_name=last_name)


def show_ninjas(dojo_name):
    dojo = Ninjas.objects.filter(dojo__name=dojo_name)
    for ninja in dojo:
        print ninja.first_name, ninja.last_name



