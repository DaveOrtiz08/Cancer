from django.contrib import admin
from .models import Intern

# Register your models here.
class InternAdmin(admin.ModelAdmin):
    list_display = ('namePa','age','date')
    list_filter = ('date',)

admin.site.register(Intern, InternAdmin)
