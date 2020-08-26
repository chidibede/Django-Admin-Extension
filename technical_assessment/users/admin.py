from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from django.urls import path
from .admin_extension_functions import set_active, set_inactive, set_staff_status, remove_staff_status
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

# change django admin site headers and titles
admin.site.site_header = "SaVests Admin Dashboard"
admin.site.site_title = "SaVests Admin Dashboard"
admin.site.index_title = "Welcome to SaVests Admin Dashboard"

# Unregister the default user here.
admin.site.unregister(User)


# Register a custom User model admin, based on the default UserAdmin
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    A Class that customizes the user admin in the django admin dashboard
    """

    # set readonly fields that do not need to be edited
    readonly_fields = [
        "date_joined",
    ]
    actions = [set_active, set_inactive, set_staff_status, remove_staff_status]

    # set how the users should be displayed in a tabular form
    list_display = ("username", "email", "is_staff", "is_active", "activate_users")
    change_list_template = "users/users_changelist_template.html"

    def get_urls(self):
        # override the get urls and set change_active_methods
        urls = super().get_urls()
        custom_admin_urls = [
            path("change_active_status/<user>", self.change_active_status),
            path("send_bulk_mails/", self.send_bulk_mails),
        ]
        return custom_admin_urls + urls

    def change_active_status(self, request, user):
        user = self.model.objects.get(username=user)
        if user.is_active == True:
            user.is_active = False
            user.save()
            self.message_user(request, "User has been deactivated")
        else:
            user.is_active = True
            user.save()
            self.message_user(request, "User has been activated")
        return HttpResponseRedirect("../")

    def activate_users(self, object):
        """
        A class method that attaches a html button to the admin dashboard
        using the format_html utility from django.utils.html
        """
        return format_html(
            f'<a class = "button" href ="change_active_status/{object.username}"> Change Active Status</a>'
        )

    def send_bulk_mails(self, request):
        subject = request.POST.get("subject")
        message = request.POST.get("body")
        users = User.objects.all()
        emails = []
        for user in users:
            emails.append(user.email)
        send_mail(
            subject,
            message,
            "chidibede@gmail.com",
            emails,
            fail_silently=True,
            auth_user=None,
            auth_password=None,
            connection=None,
            html_message=None,
        )

        self.message_user(request, "Emails sent successfully")
        return HttpResponseRedirect("../")
