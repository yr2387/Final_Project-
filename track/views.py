from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Max, Min, Count
from .models import Squirrel
from .forms import SquirrelForm
from .forms import SquirrelFormPartial
def index(request):
   squirrels = Squirrel.objects.all()
  
   context = {
        'squirrels': squirrels,
   }

   return render(request, 'track/index.html', context)

def detail(request,squirrel_id):
   squirrel = get_object_or_404(Squirrel, pk=squirrel_id)
   if request.method=='Post':
       form = SquirrelFormPartial(request.POST, instance=squirrel)
       if form.is_valid():
           form.save()
           return redirect(f'/sightings/{squirrel_id}')
   else:
       form = SquirrelFormPartial(instance=squirrel)
       context = {
            'form':form,
       }
   return render(request, 'track/detail.html', context) 

def add(request):
    if request.method=='Post':
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/')
    else:
        form = SquirrelForm()
        context = {
            'form':form
        }
    return render(request, 'track/add.html', context)

def stats(request):
    squirrels = Squirrel.objects.all()
    lattitude = squirrels.aggregate(minimum=Min('Latitude'),maximum=Max('Latitude'))
    longitude = squirrels.aggregate(minimum=Min('Longitude'),maximum=Max('Longitude'))
    age = list(squirrels.values_list('Age').annotate(Count('Age')))
    shift = list(squirrels.values_list('Shift').annotate(Count('Shift')))
    location = list(squirrels.values_list('Location').annotate(Count('Location')))
    context = {
        'lattitude': lattitude,
        'longitude': longitude,
        'age': age,
        'shift': shift,
        'location':location,
    }
    return render(request, 'track/stats.html', context)
