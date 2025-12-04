from django.db import models
from django.core.exceptions import ValidationError
import datetime

class Medico(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    horario_inicio_atendimento = models.TimeField()
    horario_fim_atendimento = models.TimeField()

    def __str__(self):
        return self.nome

class Consulta(models.Model):
    STATUS_CHOICES = [
        ('Agendada', 'Agendada'),
        ('Cancelada', 'Cancelada'),
        ('Realizada', 'Realizada'),
    ]

    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    paciente_nome = models.CharField(max_length=200)
    data = models.DateField()
    horario = models.TimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Agendada')

    def __str__(self):
        return f"Consulta de {self.paciente_nome} com {self.medico.nome} em {self.data} às {self.horario}"

    def clean(self):
        # Validação do intervalo de 30 minutos
        if self.horario.minute not in [0, 30]:
            raise ValidationError("O horário da consulta deve ser em intervalos de 30 minutos (ex: 09:00, 09:30).")

        # Validação do horário de atendimento do médico
        if not (self.medico.horario_inicio_atendimento <= self.horario < self.medico.horario_fim_atendimento):
            raise ValidationError(f"O horário da consulta está fora do horário de atendimento do médico ({self.medico.horario_inicio_atendimento} - {self.medico.horario_fim_atendimento}).")

        # Validação de sobreposição de consultas
        consultas_no_mesmo_horario = Consulta.objects.filter(
            medico=self.medico,
            data=self.data,
            horario=self.horario
        ).exclude(pk=self.pk)

        if consultas_no_mesmo_horario.exists():
            raise ValidationError("Já existe uma consulta agendada para este médico neste mesmo dia e horário.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)