from django.contrib import admin
from .Module import Module
from .File import File


# Register your models here.
admin.site.register(Module)
admin.site.register(File)