from django.contrib import admin
from .models import Bb, TypeShoses


# Register your models here.

class BbAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'adress', 'characteristics']


admin.site.register(Bb, BbAdmin)
admin.site.register(TypeShoses)
