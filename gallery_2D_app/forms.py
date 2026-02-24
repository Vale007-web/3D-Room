from django import forms
from .models import Canvas
# from .models import UserImage

# class ImageUploadForm(forms.ModelForm):
#     class Meta:
#         model = UserImage
#         fields = ['image']



class CanvasForm(forms.ModelForm):
    class Meta:
        model = Canvas
        fields = ['name', 'Canvas_Img']