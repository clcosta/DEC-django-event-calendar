from django import forms
from .models import Event


class CreateEventForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CreateEventForm, self).__init__(*args, **kwargs)
        self.fields['data_inicio'].widget.attrs.update({"class":"mask-date"})
        self.fields['data_final'].widget.attrs.update({"class":"mask-date"})

    class Meta:
        model = Event
        fields = [
            "nome",
            "descricao",
            "lv_prioridade",
            "data_inicio",
            "data_final",
        ]

class UpdateEventForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UpdateEventForm, self).__init__(*args, **kwargs)
        self.fields['data_inicio'].widget.attrs.update({"class":"mask-date"})
        self.fields['data_final'].widget.attrs.update({"class":"mask-date"})
    
    class Meta:
        model = Event
        fields = [
            "nome",
            "descricao",
            "lv_prioridade",
            "data_inicio",
            "data_final",
            "concluido",
        ]
