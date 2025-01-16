from django.urls import path
from . import views


app_name = 'users'

urlpatterns = [
    path('mi_info', views.mi_info, name='info'),
    path('MisdatosRecepcionista', views.MisdatosRecepcionista, name='MisdatosRecepcionista'),
    path('DatosDoctor', views.DatosDoctor, name='DatosDoctor'),
]