from django.contrib import admin

# Register your models here.
from .models import Analysis

class AnalysisAdmin(admin.ModelAdmin):
    list_display = ["user_id","days","created"]
    #code
    
admin.site.register(Analysis, AnalysisAdmin)
