from django.urls import path
from . import views
# from . import views

# app_name = "canvas"

# Define a list of url patterns
# urlpatterns = [
#     path('', views.gallery3d_view, name="gallery3d"),
# ]

urlpatterns = [
    path('', views.gallery_view, name='gallery'),
    path('upload/', views.upload_model, name='upload_model'),
]

