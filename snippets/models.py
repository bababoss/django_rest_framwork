from __future__ import unicode_literals
from django.forms import widgets
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


# Create your models here.


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())



class Analysis(models.Model):   
    created = models.DateTimeField(auto_now_add=True,null = True)
    user_id = models.IntegerField()
    attendance = models.CharField(max_length=10, blank=False,default=' ')
    

    class Meta:
        ordering = ('created',)
        
    def __unicode__(self):
        return str(self.user_id)
    