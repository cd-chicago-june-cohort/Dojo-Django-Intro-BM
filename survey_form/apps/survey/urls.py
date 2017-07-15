from django.conf.urls import url
from views import index, result, reset

urlpatterns = [
    url(r'^$', index),
    url(r'^result$', result),
    url(r'^reset$', reset)
]

