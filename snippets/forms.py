from django import forms
from .models import Analysis
from django.forms import widgets

class  AnalysisForm(forms.ModelForm):
    class Meta:
        model = Analysis
        fields = ['user_id']