from django.urls.base import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from .forms import CreateEventForm, UpdateEventForm
from .models import Event


class HomePage(TemplateView):
    template_name = 'home/home.html'

class CalendarPage(ListView):
    model = Event
    template_name = 'calendar/calendar.html'

    def get_queryset(self):
        object_list = Event.objects.filter(concluido=False)
        return object_list

class AddEvent(CreateView):

    model = Event
    template_name = 'eventos/form_event.html'
    form_class = CreateEventForm
    success_url = reverse_lazy("home")

class ListEvent(ListView):
    model = Event
    template_name = "eventos/list_events.html"

class DetailEvent(DetailView):
    model = Event
    template_name = "eventos/detail_event.html"

class UpdateEvent(UpdateView):

    model = Event
    template_name = "eventos/form_event.html"
    form_class = UpdateEventForm
    success_url = reverse_lazy("event:list_event")

    extra_context = {"is_update":True}


class DeteleEvent(DeleteView):
    model = Event
    template_name = "eventos/delete_event.html"
    success_url = reverse_lazy("event:list_event")

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.POST.get("delete"):
            ## Sucesso
            return super().post(request, *args, **kwargs)
        return redirect(self.success_url)
