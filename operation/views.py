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

def GestionCita(request):
    return render(request, 'operation/GestionCita.html')

def SelecionDatosRecepcionista(request):
    return render(request, 'operation/SelecionDatosRecepcionista.html')

def GestionUsuario(request):
    return render(request, 'operation/GestionUsuario.html')

def InventarioFarmacia(request):
    return render(request, 'operation/InventarioFarmacia.html')

def Venta(request):
    return render(request, 'operation/Venta.html')

def Servicios(request):
    return render(request, 'operation/Servicios.html')

def Consultorios(request):
    return render(request, 'operation/Consultorios.html')

def BuscarPaciente(request):
    return render(request, 'operation/BuscarPaciente.html')

def PersonalMedico(request):
    return render(request, 'operation/PersonalMedico.html')

def RecetasDoctor(request):
    return render(request, 'operation/RecetasDoctor.html')

def CitasDoctor(request):
    return render(request, 'operation/CitasDoctor.html')