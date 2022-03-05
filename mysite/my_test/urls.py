from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("starts/", views.v1, name="v1")
]