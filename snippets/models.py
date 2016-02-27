from __future__ import unicode_literals

from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# Create your models here.


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Analysis(models.Model):
    created = models.DateField()
    user_id = models.IntegerField(default=0)
    days = models.IntegerField(default=0)
    

    class Meta:
        ordering = ('created',)