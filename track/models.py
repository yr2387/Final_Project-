from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):
    Longitude = models.FloatField(null=False, blank=False)
    Latitude = models.FloatField(null=False, blank=False)
    Unique_Squirrel_ID = models.CharField(max_length = 100, blank=False)
    Date = models.DateField()
    Shift = models.CharField(max_length=100,blank=True)
    Age = models.CharField(max_length=100, blank=True)
    Primary_Fur_Color = models.CharField(max_length=100, blank=True)
    Location = models.CharField(max_length=100, blank=True)
    Specific_Location = models.CharField(max_length=100, blank=True)
    Running = models.BooleanField(null=True, blank=True)
    Chasing = models.BooleanField(null=True, blank=True)
    Climbing = models.BooleanField(null=True, blank=True)
    Eating = models.BooleanField(null=True, blank=True)
    Foraging = models.BooleanField(null=True, blank=True)
    Other_Activities = models.CharField(max_length=100, blank=True)
    Kuks = models.BooleanField(null=True, blank=True)
    Quaas = models.BooleanField(null=True, blank=True)
    Moans = models.BooleanField(null=True, blank=True)
    Tail_Flags = models.BooleanField(null=True, blank=True)
    Tail_Twitches = models.BooleanField(null=True, blank=True)
    Approaches = models.BooleanField(null=True, blank=True)
    Indifferent = models.BooleanField(null=True, blank=True)
    Runs_From = models.BooleanField(null=True, blank=True)
    def __str__(self):
        return self.Unique_Squirrel_ID

# Create your models here.
