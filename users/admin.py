from django.contrib import admin
from .models import Paciente, Trabajador, Doctor, Recepcionista
# Register your models here.


admin.site.register(Paciente)
admin.site.register(Trabajador)
admin.site.register(Doctor)
admin.site.register(Recepcionista)
