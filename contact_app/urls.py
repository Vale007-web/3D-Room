from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contact/", views.contact, name="contact"),
    path("contact/success", views.index, name="contact-success")
]       #in path: rotta principale, vista importata, nome rotta (univoco)
