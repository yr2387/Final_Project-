from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):
    Squirrel_ID = models.CharField(
        max_length = 100,
        help_text =_('Unique ID of the squirrel')
    )
    Date = models.DateField(
        help_text = _('Date')
    )
    
    def __str__(self):
        return self.Squirrel_ID

# Create your models here.
