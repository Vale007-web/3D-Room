from django.contrib import admin
from .models import Canvas

@admin.register(Canvas)
class CanvasAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')
    list_filter = ('user',)
    search_fields = ('name', 'user__username')

