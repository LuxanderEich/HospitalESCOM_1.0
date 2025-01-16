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

def AppointmentPage(request):
    return render(request, 'operation/AppointmentPage.html')

def BuscarMedicamento(request):
    return render(request, 'operation/BuscarMedicamento.html')

def ConsultarCita(request):
    return render(request, 'operation/ConsultarCita.html')