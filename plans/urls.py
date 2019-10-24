from django.urls import path
from . import views

#This is where we teach Django what the paths of our website will be
urlpatterns = [
    #path(directory, view location, name value)
    path('', views.index, name='index'),
    path('oversikt/', views.oversikt, name='oversikt'),
]