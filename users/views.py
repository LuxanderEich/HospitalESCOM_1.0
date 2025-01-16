from django.shortcuts import render


def mi_info(request):
    return render(request, 'users/personainfo.html')

def MisdatosRecepcionista(request):
    return render(request, 'users/MisdatosRecepcionista.html')

def DatosDoctor(request):
    return render(request, 'users/DatosDoctor.html')
