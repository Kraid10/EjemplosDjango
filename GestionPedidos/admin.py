from django.contrib import admin
from GestionPedidos.models import Clientes, Articulos, pedidos
# Register your models here.

class AdminClientes(admin.ModelAdmin):
    list_display=("nombre", "email")
    search_fields=("nombre", "tel")

class AdminArticulos(admin.ModelAdmin):
    list_filter=("seccion",)

class AdminPedidos(admin.ModelAdmin):
    list_display=("numero", "fecha")
    list_filter=("fecha",)
    date_hierarchy="fecha"


admin.site.register(Clientes, AdminClientes)
admin.site.register(Articulos, AdminArticulos)
admin.site.register(pedidos, AdminPedidos)



