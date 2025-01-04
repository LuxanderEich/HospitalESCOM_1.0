from django.contrib import admin
from django import forms
from .models import Datos, Direccion, Especialidad, Horario, Consultorio

# Register your models here.
admin.site.register(Datos)
admin.site.register(Direccion)
admin.site.register(Especialidad)
admin.site.register(Consultorio)


class HorarioAdminForm(forms.ModelForm):
    dias_trabaja = forms.MultipleChoiceField(
        choices=Horario.DIAS_SEMANA,
        widget=forms.CheckboxSelectMultiple,
        label="Días que trabaja",
        required=False  # Permite que el campo sea opcional
    )

    class Meta:
        model = Horario
        fields = '__all__'

    def clean_dias_trabaja(self):
        # Validación adicional si es necesario
        dias = self.cleaned_data.get('dias_trabaja', [])
        if not dias:
            raise forms.ValidationError("Debe seleccionar al menos un día.")
        return dias


@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    form = HorarioAdminForm
    list_display = ('id_horario', 'turno', 'hora_inicio', 'hora_fin', 'get_dias_trabaja')

    def get_dias_trabaja(self, obj):
        """Convierte los días almacenados en un string amigable."""
        if not obj.dias_trabaja:
            return "No especificado"
        dias = dict(Horario.DIAS_SEMANA)  # Convierte las opciones en un diccionario
        dias_trabaja = obj.dias_trabaja.split(",")  # Asume que están almacenados como una lista separada por comas
        return ', '.join([dias.get(d, d) for d in dias_trabaja])

    get_dias_trabaja.short_description = "Días que trabaja"
