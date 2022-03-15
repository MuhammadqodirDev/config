from atexit import register
from django.contrib import admin
from .models import *
# Register your models here.



admin.site.register(About)
admin.site.register(Products)
admin.site.register(Video)
admin.site.register(Client_feedback)
admin.site.register(Information)
admin.site.register(Cause)
admin.site.register(Chat_id)