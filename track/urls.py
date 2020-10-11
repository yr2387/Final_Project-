
from django.urls import path

from . import views

app_name = 'track'

urlpatterns = [
    path('', views.index, name = 'sightings'),
    path('<int:squirrel_id>/', views.detail, name = 'detail'),
    path('add/', views.add, name = 'add'),
    path('stats/', views.stats, name = 'stats')
]
