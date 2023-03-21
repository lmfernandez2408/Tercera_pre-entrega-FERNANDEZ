from django.contrib import admin
from app_morrison.models import Clientes, Pedidos, Personal

# Register your models here.

admin.site.register(Clientes)
admin.site.register (Pedidos)
admin.site.register (Personal)