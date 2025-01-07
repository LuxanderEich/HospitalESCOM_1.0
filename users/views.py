from django.shortcuts import render


def mi_info(request):
    return render(request, 'users/personainfo.html')
