from django.urls import path
from . import views
from .views import canvas_view#, success
from django.conf import settings
from django.conf.urls.static import static

# app_name = "canvas"

# Define a list of url patterns
urlpatterns = [
    path('', views.canvas_view, name="canvas"),
    path('', canvas_view, name='image_upload'),
    #path('success/', success, name='success'),
    path('delete/<int:image_id>/', views.delete_image, name='delete_image'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)