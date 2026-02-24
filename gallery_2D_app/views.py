from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import CanvasForm
from .models import Canvas


def canvas_view(request):
     # Recupero di tutte le immagini salvate
    images = Canvas.objects.filter(user=request.user)
    
    if request.method == 'POST':
        form = CanvasForm(request.POST, request.FILES)
        if form.is_valid():
            canvas = form.save(commit=False)  # non salvare subito
            canvas.user = request.user       # collega l’immagine all’utente
            form.save()
            return redirect('canvas')
            # return redirect('success')
    else:
        form = CanvasForm()

    return render(request, 'gallery_2D.html', {
        'form': form,
        'images': images
        })

# def success(request):
#     return HttpResponse('Successfully uploaded!')


# Cancellare le immagini
def delete_image(request, image_id):
    image = get_object_or_404(Canvas, id=image_id)

    # Controlla che l’utente loggato sia il proprietario
    if image.user == request.user:
        image.delete()
    else:
        # opzionale: puoi mostrare un messaggio di errore
        pass

    return redirect('canvas')  # torna alla pagina canvas