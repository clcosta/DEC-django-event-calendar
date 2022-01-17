from django.urls.base import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView

from .models import Event


class HomePage(TemplateView):
    template_name = 'home/home.html'

class CalendarPage(ListView):
    model = Event
    template_name = 'calendar/calendar.html'

class AddEvent(CreateView):

    model = Event
    template_name = 'calendar/form_event.html'

    success_url = reverse_lazy("home")
    fields = ["nome", "descricao", "lv_prioridade", "data_inicio", "data_final"]