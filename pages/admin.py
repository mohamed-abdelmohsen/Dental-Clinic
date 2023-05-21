from django.contrib import admin
from .models import patient,searchModel


# Register your models here.
class patientadmin(admin.ModelAdmin):
    search_fields=['id']
    list_display=['name','id']

admin.site.register(patient,patientadmin)
admin.site.register(searchModel)



admin.site.site_header='Teeth lap'
admin.site.site_title='Teeth lap'
