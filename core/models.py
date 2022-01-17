from random import choices
from django.utils import timezone
from django.db import models
from django.conf import settings

priority_choices = (
    (1, "Baixa"),
    (2, "Média"),
    (3, "Alta"),
    (4, "Critica"),
)

def get_data_final():
    if hasattr(settings, 'TEMPO_EVENTO'):
        return timezone.now() + timezone.timedelta(minutes=settings.TEMPO_EVENTO)
    return timezone.now() + timezone.timedelta(minutes=60)

class Event(models.Model):

    nome = models.CharField(max_length=150)

    descricao = models.TextField(max_length=500)

    lv_prioridade = models.PositiveIntegerField(choices=priority_choices)

    @property
    def priority(self):
        dict_priority = dict(priority_choices)
        for lvl in dict_priority:
            if lvl == self.lv_prioridade:
                return dict_priority[lvl]

    data_inicio = models.DateTimeField(default=timezone.now)
    data_final = models.DateTimeField(default=get_data_final)
    data_criacao = models.DateTimeField(default=timezone.now)

    concluido = models.BooleanField(default=False)

    @property
    def conclusao(self):
        if self.concluido: return "Concluído"
        return "Pendente"

    def __str__(self):
        return f"{self.nome} - {self.priority} - {self.conclusao}"
    

    class Meta:
        verbose_name_plural = "Eventos"
