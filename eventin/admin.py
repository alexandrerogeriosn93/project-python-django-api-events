from django.contrib import admin
from .models import Event, Participant

class Events(admin.ModelAdmin):
    list_display = ('id', 'title', 'local', 'date_event', 'capacity')
    list_display_links = ('id', 'title')
    list_per_page = 20
    search_fields = ('title', 'local')


admin.site.register(Event, Events)

class Participants(admin.ModelAdmin):
    list_display = ('id', 'name', 'cpf', 'email', 'phone')
    list_display_links = ('id', 'name')
    list_per_page = 20
    search_fields = ('name', 'email')


admin.site.register(Participant, Participants)
