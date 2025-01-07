from django.urls import path
from . import views


app_name = 'users'

urlpatterns = [
    path('users/mi_info', views.mi_info, name='info')
]