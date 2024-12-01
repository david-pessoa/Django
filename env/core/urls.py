from core import views as v
from django.urls import path
from django.conf.urls import handler404, handler500
from .views import *

urlpatterns = [
    path('', index),
    path('contato', contato),
    path('produto/<int:pk>', produto, name='produto'),
    path('teste', teste)
]

handler404 = v.error404
handler500 = v.error500