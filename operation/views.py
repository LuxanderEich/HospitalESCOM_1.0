from django.shortcuts import render


def registro(request):
    return render(request, 'operation/registro1.html')


def informacion(request):
    return render(request, 'operation/registro2.html')


def login(request):
    return render(request, 'operation/login.html')


def agendar_cita(request):
    return render(request, 'operation/agendar_cita.html')

def ContactUsPage(request):
    return render(request, 'operation/ContactUsPage.html')

def BuscarMedicamento(request):
    return render(request, 'operation/BuscarMedicamento.html')

def ConsultarCita(request):
    return render(request, 'operation/ConsultarCita.html')

def ModificarDatos(request):
    return render(request, 'operation/ModificarDatos.html')

def InfoSanitaria(request):
    return render(request, 'operation/InfoSanitaria.html')

def CancelarCita(request):
    return render(request, 'operation/CancelarCita.html')

def Recetas(request):
    return render(request, 'operation/Recetas.html')

def buscarmedico(request):
    return render(request, 'operation/buscarmedico.html')

def DepMedicos(request):
    return render(request, 'operation/DepMedicos.html')