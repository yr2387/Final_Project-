import csv

from django.core.management.base import BaseCommand, CommandError
from track.models import Squirrel


class Command(BaseCommand):
    help = 'Eexport the data'

    def add_arguments(self, parser):
        parser.add_argument('args', type=str, nargs='*')

    def handle(self, *args, **kwargs):
        path = args[0]
        fields = Squirrels._meta.fields
        with open(path, 'w') as f:
            writer = csv.writer(f, quoting = csv.QUOTE_ALL)
            for item in Squirrels.objects.all():
                row = [getattr(item, field.name) for field in fields]
                writer.writerow(row)
            f.close()
