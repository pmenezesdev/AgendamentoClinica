from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('medicos/', views.medicos_list, name='medicos_list'),
    path('agendar/', views.agendar_consulta, name='agendar_consulta'),
    path('agendar/<int:medico_id>/', views.agendar_consulta, name='agendar_consulta_com_medico'),
]
