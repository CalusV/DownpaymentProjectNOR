from django.urls import include, path
from . import views

# urls.py brukes til å fortelle Django hvor vi vil dirigere trafikk dersom brukere besøker forskjellige URL

urlpatterns = [
    #path(directory, view location, name value)
    path('', views.index, name='index'),
    path('oversikt/', views.oversikt, name='oversikt'),
]