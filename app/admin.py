from django.contrib import admin

# Register your models here.
from app.models import *
admin.site.register(Song)
admin.site.register(Playlist)