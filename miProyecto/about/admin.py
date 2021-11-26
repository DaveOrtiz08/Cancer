from django.contrib import admin
from .models import Body

# Register your models here.
class BodyAdmin(admin.ModelAdmin):
    list_display = ('zones','porcent','tratamient')
    list_filter = ('porcent',)

admin.site.register(Body, BodyAdmin)
