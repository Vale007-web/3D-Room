"""
URL configuration for room3d project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin                    # per l’interfaccia di amministrazione di Django.
from django.urls import path, include               # path per definire singole rotte; include per includere file urls.py di altre app, utile per organizzare il progetto.
from django.conf import settings                    # per accedere alle impostazioni del progetto (DEBUG, MEDIA_URL, ecc.).
from django.conf.urls.static import static          # per servire file statici e media in modalità sviluppo (DEBUG=True).

urlpatterns = [                                     # Vengono definite le URL principali
    path('admin/', admin.site.urls),                # porta all’interfaccia admin di Django.
    path('', include('gallery_TO_app.urls')),
    path('', include('contact_app.urls')),
    path('', include('auth_app.urls')),
    path('canvas/', include('gallery_2D_app.urls')),
    path('gallery3d/', include('gallery_3D_app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
