from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Punti predefiniti nella stanza
POSITION_CHOICES = [
    ('luogo1', 'Luogo 1'),
    ('luogo2', 'Luogo 2'),
    ('luogo3', 'Luogo 3'),
]

# Coordinate XYZ corrispondenti ai punti
POSITION_COORDS = {
    'luogo1': (0, 0, -5),
    'luogo2': (5, 0, 0),
    'luogo3': (-5, 0, 0),
}

# Posizione salvataggio files
def user_canvas_directory_path(instance, filename):
    return f'user_{instance.user.id}/gallery_3Dmodels_user_{instance.user.id}/{filename}'

class Model3D(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    model_file = models.FileField(upload_to=user_canvas_directory_path)
    position_choice = models.CharField(max_length=10, choices=POSITION_CHOICES)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    scale = models.FloatField(default=1.0)  # dimensione del modello

    def get_coordinates(self):
        return POSITION_COORDS[self.position_choice]

    def __str__(self):
        return self.title
