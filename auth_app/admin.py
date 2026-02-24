from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from gallery_2D_app.models import Canvas
from gallery_3D_app.models import Model3D

class CanvasInline(admin.TabularInline):
    model = Canvas
    extra = 0

class Model3DInline(admin.TabularInline):
    model = Model3D
    extra = 0

class UserAdmin(BaseUserAdmin):
    inlines = [CanvasInline, Model3DInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

