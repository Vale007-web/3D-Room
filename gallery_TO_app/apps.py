from django.apps import AppConfig           # Importa la classe base che Django usa per configurare un'app.


class GalleryTOAppConfig(AppConfig):                                # Crea la configurazione dell’app.
    default_auto_field = 'django.db.models.BigAutoField'        # Il nome della classe finisce con Config per convenzione.
    name = 'gallery_TO_app'                                          # Questo nome deve corrispondere alla cartella dell'app e a quello inserito in INSTALLED_APPS nel file settings.py.  
