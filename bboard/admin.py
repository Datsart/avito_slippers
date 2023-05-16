from django.contrib import admin
from .models import Bb, Condition, Size


# Register your models here.

class BbAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'description']


admin.site.register(Bb, BbAdmin)
admin.site.register(Condition)
admin.site.register(Size)
# admin.site.register(Сharacteristic)
