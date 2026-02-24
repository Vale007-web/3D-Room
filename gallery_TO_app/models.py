from django.db import models    # importa il modulo models di Django che crea le tabelle scritte di seguito come "class"
from django.contrib.auth.models import User as AuthUser     # rinomino user di django in authuser per non interferire con user che ho creato io

# Create your models here.
class User(models.Model):       
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()
    bio = models.TextField(blank=True)
    hobby = models.CharField(max_length=200, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    user = models.OneToOneField(AuthUser, on_delete=models.CASCADE, null=True)

    # objects = UserQuerySet.as_manager()

    def __str__(self):
        return f'nome: {self.name} cognome: {self.surname} age: {self.age}'
    

class Model3D(models.Model):
    artist = models.ForeignKey(User, on_delete=models.CASCADE, related_name="models")
    title = models.CharField(max_length=50)
    description = models.TextField()
    file = models.FileField(upload_to='models/')
    thumbnail = models.ImageField(upload_to='thumbnails/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class RenderImage(models.Model):
    model = models.ForeignKey(Model3D, on_delete=models.CASCADE, related_name="images")
    file = models.ImageField(upload_to='renders/')
    created_at = models.DateTimeField(auto_now_add=True)


class GallerySettings(models.Model):
    artist = models.OneToOneField(User, on_delete=models.CASCADE)
    light_color = models.CharField(max_length=20, default="#ffffff")
    light_intensity = models.FloatField(default=1.0)
    floor_texture = models.CharField(max_length=100, default="default_floor.jpg")
    wall_texture = models.CharField(max_length=100, default="default_wall.jpg")
    pedestal_type = models.CharField(max_length=50, default="standard")
    frame_type = models.CharField(max_length=50, default="classic")




# class UserImage(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='images')
#     image = models.ImageField(upload_to='user_images/')
#     description = models.CharField(max_length=255, blank=True)
#     pos_x = models.IntegerField(default=0)
#     pos_y = models.IntegerField(default=0)
#     uploaded_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Image {self.id} of {self.user.username}"










# class Artist(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField(blank=True)
#     avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

#     def __str__(self):
#         return self.user.username


# class Model3D(models.Model):
#     artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="models")
#     title = models.CharField(max_length=150)
#     description = models.TextField()
#     file = models.FileField(upload_to='models/')
#     thumbnail = models.ImageField(upload_to='thumbnails/')
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title


# class RenderImage(models.Model):
#     model = models.ForeignKey(Model3D, on_delete=models.CASCADE, related_name="images")
#     file = models.ImageField(upload_to='renders/')
#     created_at = models.DateTimeField(auto_now_add=True)


# class GallerySettings(models.Model):
#     artist = models.OneToOneField(Artist, on_delete=models.CASCADE)
#     light_color = models.CharField(max_length=20, default="#ffffff")
#     light_intensity = models.FloatField(default=1.0)
#     floor_texture = models.CharField(max_length=100, default="default_floor.jpg")
#     wall_texture = models.CharField(max_length=100, default="default_wall.jpg")
#     pedestal_type = models.CharField(max_length=50, default="standard")
#     frame_type = models.CharField(max_length=50, default="classic")
