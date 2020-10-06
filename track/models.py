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

# Create your models here.
