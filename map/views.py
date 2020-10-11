from django.shortcuts import render
from track.models import Squirrel

# Create your views here.
def map(request):
    squirrel_map = Squirrel.objects.all()[:100]
    return render(request, 'map/map.html', {"squirrel_map":squirrel_map})
