from django.contrib import admin
from .models import User, Model3D, RenderImage, GallerySettings
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User as AuthUser
from .models import User

# Register your models here.
admin.site.register(User)
admin.site.register(Model3D)
admin.site.register(RenderImage)
admin.site.register(GallerySettings)


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class UserInline(admin.StackedInline):
    model = User
    can_delete = False
    verbose_name_plural = "user"


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = [UserInline]


# Re-register UserAdmin
admin.site.unregister(AuthUser)
admin.site.register(AuthUser, UserAdmin)