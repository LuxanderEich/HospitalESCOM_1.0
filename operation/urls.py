from django.urls import path
from . import views

app_name = 'operation'

urlpatterns = [
    path("registro", views.registro, name="registro"),
    path("registro/informacion", views.informacion, name="informacion"),
    path("login", views.login, name="login"),
    path("agendar_cita", views.agendar_cita, name="agendar_cita"),
    path("ContactUsPage", views.ContactUsPage, name="ContactUsPage"),
    path("BuscarMedicamento", views.BuscarMedicamento, name="BuscarMedicamento"),
    path("ConsultarCita", views.ConsultarCita, name="ConsultarCita"),
    path("ModificarDatos", views.ModificarDatos, name="ModificarDatos"),
    path("InfoSanitaria", views.InfoSanitaria, name="InfoSanitaria"),
    path("CancelarCita", views.CancelarCita, name="CancelarCita"),
    path("Recetas", views.Recetas, name="Recetas"),
    path("buscarmedico", views.buscarmedico, name="buscarmedico"),
    path("DepMedicos", views.DepMedicos, name="DepMedicos"),
    path("GestionCita", views.GestionCita, name="GestionCita"),
    path("SelecionDatosRecepcionista", views.SelecionDatosRecepcionista, name="SelecionDatosRecepcionista"),
    path("GestionUsuario", views.GestionUsuario, name="GestionUsuario"),
    path("InventarioFarmacia", views.InventarioFarmacia, name="InventarioFarmacia"),
    path("Venta", views.Venta, name="Venta"),
    path("Servicios", views.Servicios, name="Servicios"),
    path("Consultorios", views.Consultorios, name="Consultorios"),
    path("BuscarPaciente", views.BuscarPaciente, name="BuscarPaciente"),
    path("PersonalMedico", views.PersonalMedico, name="PersonalMedico"),

]
