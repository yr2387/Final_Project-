from django.shortcuts import render
from track.models import Squirrel

def map(request):
    squirrelmap = Squirrel.objects.all()
    return render(request, 'map/map.html', {"squirrelmap":squirrelmap})


