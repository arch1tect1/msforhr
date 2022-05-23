from django.contrib import admin
from .models import File


class ModelFile(admin.ModelAdmin):
    list_display = ('name', 'date', 'comments', 'pdf')

admin.site.register(File, ModelFile)
