from django.contrib import admin
from .models import Pacientes, Tessiu

# Register your models here.

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Pacientes, PacienteAdmin)


class TessiuAdmin(admin.ModelAdmin):
    list_display = ('color','temperatura','inflammation')
    list_filter = ('color',)
    #readonly_fields=('color',)
    ordering = ('color',)
    search_fields=('color',)

admin.site.register(Tessiu, TessiuAdmin)
