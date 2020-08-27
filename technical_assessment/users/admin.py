from django.contrib import admin
from django.contrib.auth.models import User
from .admin_extension_class import CustomUserAdmin


# change django admin site headers and titles
admin.site.site_header = "SaVests Admin Dashboard"
admin.site.site_title = "SaVests Admin Dashboard"
admin.site.index_title = "Welcome to SaVests Admin Dashboard"

# Unregister the default user here.
admin.site.unregister(User)


# Register a custom User model admin, based on the default UserAdmin from the admin_extension file
admin.site.register(User, CustomUserAdmin)
