from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Model3D
from .forms import Model3DForm

# Create your views here.
def gallery_view(request):
    models = Model3D.objects.filter(user=request.user)

    if request.method == 'POST':
        form = Model3DForm(request.POST, request.FILES)
        if form.is_valid():
            model = form.save(commit=False)
            model.user = request.user
            model.save()
            return redirect('gallery')
    else:
        form = Model3DForm()

    return render(request, 'gallery_3D.html', {'form': form, 'models': models})

def delete_model(request, model_id):
    model = get_object_or_404(Model3D, id=model_id)
    if model.user == request.user:
        if model.model_file:
            model.model_file.delete(save=False)
        model.delete()
    return redirect('gallery')

# @login_required
# def gallery_view(request):
#     models = Model3D.objects.filter(user=request.user)
#     form = Model3DForm()
#     return render(request, 'gallery_3D.html', {
#         'models': models,
#         'form': form,
#     })

@login_required
def upload_model(request):
    if request.method == 'POST':
        form = Model3DForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
    return redirect('gallery3d')