from django.contrib import admin
from .models import Model3D

@admin.register(Model3D)
class Model3DAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'position_choice', 'uploaded_at')
    list_filter = ('user', 'position_choice', 'uploaded_at')
    search_fields = ('title', 'user__username')

