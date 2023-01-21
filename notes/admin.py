from django.contrib import admin
from notes.models import Note
# Register your models here.
# admin.site.register(Note)

#this will help us customize the table 
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display =['titel', 'created_day']
    # the list should be exist in the models
