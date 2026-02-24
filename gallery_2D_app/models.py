from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver

# percorso di salvataggio files diverso per ogni utente
def user_canvas_directory_path(instance, filename):
    # Salva le immagini in: media/user_<id>/canvas_images_user_<id>/<filename>
    return f'user_{instance.user.id}/canvas_images_user_{instance.user.id}/{filename}'


# Create your models here.
class Canvas(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    Canvas_Img = models.ImageField(upload_to=user_canvas_directory_path)             # ImageField is used for image uploads.

    def __str__(self):
        return self.name
    

# Eliminare anche il file fisico oltre al file nella pagina
@receiver(post_delete, sender=Canvas)
def delete_canvas_file(sender, instance, **kwargs):
    if instance.Canvas_Img:
        instance.Canvas_Img.delete(save=False)
