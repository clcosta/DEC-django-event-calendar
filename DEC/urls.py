from django.contrib import admin
from django.urls import path, include
from core import views


urlpatterns = [
    path('admin/', admin.site.urls),
    ## My urls
    path('', views.HomePage.as_view(), name='home'),
    path('calendario/', views.CalendarPage.as_view(), name="calendar"),
    path("event/", include(("core.urls", "event"), namespace="event")),
]
