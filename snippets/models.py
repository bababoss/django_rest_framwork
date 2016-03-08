from __future__ import unicode_literals
from django.forms import widgets
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


# Create your models here.


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

YEAR_CHOICES = ('2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023','2024','2025','2026','2027')
MONTH_CHOICES = ('January','february','march','april','may','june','july','august','november','december')


class Analysis(models.Model):   
    created = models.DateTimeField(auto_now_add=True,null = True)
    user_id = models.IntegerField(default=0)
    days = models.IntegerField(default=0)
    

    class Meta:
        ordering = ('created',)