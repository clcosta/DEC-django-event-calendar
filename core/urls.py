from django.urls import path

from . import views

urlpatterns = [
    path("add/", views.AddEvent.as_view(), name="add_event"),
    path("list/", views.ListEvent.as_view(), name="list_event"),
    path("detail/<int:pk>/", views.DetailEvent.as_view(), name="detail_event"),
    path("update/<int:pk>/", views.UpdateEvent.as_view(), name="update_event"),
    path("delete/<int:pk>/", views.DeteleEvent.as_view(), name="delete_event"),
]
