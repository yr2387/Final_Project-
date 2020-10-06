
from django.urls import path

from . import views

app_name = 'track'

urlpatterns = [
    path('', views.index),
    path('<int:squirrel_id>/', views.detail, name = 'detail')
]
