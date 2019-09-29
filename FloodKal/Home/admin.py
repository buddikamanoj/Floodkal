from django.contrib import admin
from django import forms
from .models import Map

class MapAdminForm(forms.ModelForm):

    class Meta:
        model = Map
        fields = '__all__'


class MapAdmin(admin.ModelAdmin):
    form = MapAdminForm
    list_display = ['LocName']
    readonly_fields = ['LocName']

admin.site.register(Map, MapAdmin)


