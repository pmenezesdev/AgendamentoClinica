from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Medico, Consulta
from datetime import time, timedelta, datetime

def medicos_list(request):
    """
    View para listar todos os médicos.
    """
    medicos = Medico.objects.all()
    return render(request, 'core/medicos_list.html', {'medicos': medicos})

def agendar_consulta(request, medico_id=None):
    """
    View para agendar uma nova consulta com lógica de encaixe inteligente.
    """
    medicos = Medico.objects.all()
    selected_medico = None
    message = None
    message_type = None # 'success' or 'error'

    if medico_id:
        selected_medico = get_object_or_404(Medico, pk=medico_id)

    if request.method == 'POST':
        medico_id_form = request.POST.get('medico_id')
        paciente_nome = request.POST.get('paciente_nome')
        data_str = request.POST.get('data')

        if not all([medico_id_form, paciente_nome, data_str]):
            message = "Erro: Todos os campos são obrigatórios."
            message_type = 'error'
        else:
            medico = get_object_or_404(Medico, pk=medico_id_form)
            data = datetime.strptime(data_str, '%Y-%m-%d').date()

            # Lógica para encontrar o primeiro horário disponível
            horarios_agendados = Consulta.objects.filter(medico=medico, data=data, status__in=['Agendada', 'Realizada']).values_list('horario', flat=True)

            horario_atual = datetime.combine(data, medico.horario_inicio_atendimento)
            horario_fim = datetime.combine(data, medico.horario_fim_atendimento)
            
            horario_disponivel = None

            while horario_atual.time() < horario_fim.time():
                # Verifica se o horário atual e o próximo horário (30 min depois) estão dentro do expediente
                if horario_atual.time() >= medico.horario_inicio_atendimento and \
                   (horario_atual + timedelta(minutes=30)).time() <= medico.horario_fim_atendimento:
                    
                    if horario_atual.time() not in horarios_agendados:
                        horario_disponivel = horario_atual.time()
                        break
                horario_atual += timedelta(minutes=30)

            if horario_disponivel:
                try:
                    nova_consulta = Consulta(
                        medico=medico,
                        paciente_nome=paciente_nome,
                        data=data,
                        horario=horario_disponivel,
                        status='Agendada'
                    )
                    nova_consulta.full_clean() # Valida o modelo antes de salvar (incluindo o clean method)
                    nova_consulta.save()
                    message = f"Consulta agendada com sucesso para {data.strftime('%d/%m/%Y')} às {horario_disponivel.strftime('%H:%M')}!"
                    message_type = 'success'
                except Exception as e:
                    message = f"Erro ao agendar consulta: {e}"
                    message_type = 'error'
            else:
                message = f"Não há horários disponíveis para o(a) Dr(a). {medico.nome} na data {data.strftime('%d/%m/%Y')}."
                message_type = 'error'
        
        # Se a requisição foi POST, tentamos preencher selected_medico novamente
        if medico_id_form:
            selected_medico = get_object_or_404(Medico, pk=medico_id_form)


    context = {
        'medicos': medicos,
        'selected_medico': selected_medico,
        'message': message,
        'message_type': message_type,
    }
    return render(request, 'core/agendar_consulta.html', context)