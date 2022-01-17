from django.contrib import admin

from core.models import Event as eventos

@admin.register(eventos)
class EventAdmin(admin.ModelAdmin):

    search_fields = ("nome","data_criacao")