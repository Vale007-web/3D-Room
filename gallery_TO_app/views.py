from django.shortcuts import render, redirect
from .models import User   # <-- il tuo modello custom
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required                                 # se l’utente non è loggato, Django lo manda al login.
def index(request):
    return render(request, 'index.html')        # restituisce il template index.html