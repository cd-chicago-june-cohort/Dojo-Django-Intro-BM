from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^users$', users),
    url(r'^users/new$', newuser),
    url(r'^users/create$', createuser),
    url(r'^users/edit/(?P<user_id>\d+)$', edituser),
    url(r'^users/show/(?P<user_id>\d+)$', showuser),
    url(r'^users/delete/(?P<user_id>\d+)$', deleteuser),
    url(r'^users/finaledit/(?P<user_id>\d+)$', finaledit)
]