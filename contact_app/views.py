from django.shortcuts import render, redirect
from .forms import ContactForm
# from django.contrib.auth.decorators import login_required
# Create your views here.

# homepage
# @login_required
def index(request):
    return render(request, 'index.html')

# modulo_di_contatto
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            #invia email
            form.send_email()
            return redirect('contact-success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

# pagina di successo di contatto
def contact_success(request):
    return render(request, 'contact_success.html')