from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin
from .models import *
# Register your models here.
admin.site.register(Chat)
admin.site.register(Message)