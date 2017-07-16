from django.conf.urls import url
from views import index, newword, reset

urlpatterns = [
    url(r'^$', index),
    url(r'^newword$', newword),
    url(r'^reset$', reset)
]