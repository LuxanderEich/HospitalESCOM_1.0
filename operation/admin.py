from django.contrib import admin
from .models import Citas, Pago, Receta, Diagnostico, Medicamento, Tratamiento, Inventario, Venta, Servicio
# Register your models here.


admin.site.register(Citas)
admin.site.register(Pago)
admin.site.register(Receta)
admin.site.register(Diagnostico)
admin.site.register(Medicamento)
admin.site.register(Tratamiento)
admin.site.register(Inventario)
admin.site.register(Venta)
admin.site.register(Servicio)