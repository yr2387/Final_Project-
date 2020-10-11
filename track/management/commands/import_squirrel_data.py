from django.core.management import BaseCommand
from track.models import Squirrel
import csv

class Command(BaseCommand):
    help = 'import squirrel data from csv file'

    def add_arguments(self, parser):
        parser.add_argument('path',type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'r') as f:
            reader = csv.reader(f,dialect='excel')
            next(reader)
            for row in reader:
                squirrle = Squirrel.objects.get_or_create(
                    Latitude = row[0],
                    Longitude= row[1],
                    Unique_Squirrel_ID = row[2],
                    Shift = row[4],
                    Date = row[5][4:8]+'-'+ row[5][0:2]+'-'+ row[5][2:4],
                    Age = row[7],
                    Primary_Fur_Color = row[8],
                    Location = row[12],
                    Specific_Location = row[14],
                    Running = True if row[15].lower()=='true' else False,
                    Chasing = True if row[16].lower()=='true' else False,
                    Climbing = True if row[17].lower()=='true' else False,
                    Eating = True if row[18].lower()=='true' else False,
                    Foraging = True if row[19].lower()=='true' else False,
                    Other_Activities = row[20],
                    Kuks = True if row[21].lower()=='true' else False,
                    Quaas = True if row[22].lower()=='true' else False,
                    Moans = True if row[23].lower()=='true' else False,
                    Tail_Flags = True if row[24].lower()=='true' else False,
                    Tail_Twitches = True if row[25].lower()=='true' else False,
                    Approaches = True if row[26].lower()=='true' else False,
                    Indifferent = True if row[27].lower()=='true' else False,
                    Runs_From = True if row[28].lower()=='true' else False,)
