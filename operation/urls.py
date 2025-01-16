from django.urls import path
from . import views

app_name = 'operation'

urlpatterns = [
    path("registro", views.registro, name="registro"),
    path("registro/informacion", views.informacion, name="informacion"),
    path("login", views.login, name="login"),
    path("agendar_cita", views.agendar_cita, name="agendar_cita"),
    path("ContactUsPage", views.ContactUsPage, name="ContactUsPage"),

]
