from django.urls import path, include                      # path → definisce  una singola rotta; include → collega altre app.
from .views import index                                   # Importa la funzione index dal file views.py della stessa app.

# Define a list of url patterns
urlpatterns = [
    path('', index, name="index"),                         # Questa è la homepage (URL vuoto = /). non scrive nulla nell'url, chiama la view index, le da il nome simbolico di index
]