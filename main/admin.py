from django.contrib import admin
from django.db.models import query
from .models import Departamento_agencia,Provincia_agencia,Distrito_agencia,Usuario_agencia,Galeria_agencia,Evento_agencia,Recorrido_agencia,Servicios_agencia,Paquete_turistico_agencia
# Register your models here.

admin.site.register(Usuario_agencia)
admin.site.register(Departamento_agencia)
admin.site.register(Provincia_agencia)
admin.site.register(Distrito_agencia)
admin.site.register(Galeria_agencia)
admin.site.register(Evento_agencia)
admin.site.register(Recorrido_agencia)
admin.site.register(Servicios_agencia)
admin.site.register(Paquete_turistico_agencia)
admin.site.site_header="Agencia de Turismo Pureq Runa Tours"
admin.site.index_title="Agencia de Turismo Pureq Runa Tours"
admin.site.site_title="Agencia de Turismo Pureq Runa Tours"