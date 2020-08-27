import json
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from django.urls import path
from .admin_actions_functions import (
    set_active,
    set_inactive,
    set_staff_status,
    remove_staff_status,
)
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.db.models.functions import TruncDay, TruncWeek, TruncMonth
from django.db.models.aggregates import Count
from django.core.serializers.json import DjangoJSONEncoder

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
    change_list_template = "users/admin/User/change_list.html"

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

    def changelist_view(self, request, extra_context=None):
        # Aggregate new subscribers per day
        daily_chart_data = (
            User.objects.annotate(date=TruncDay("date_joined"))
            .values("date")
            .annotate(y=Count("id"))
            .order_by("-date")
        )

        # Aggregate new subscribers per day
        weekly_chart_data = (
            User.objects.annotate(date=TruncWeek("date_joined"))
            .values("date")
            .annotate(y=Count("id"))
            .order_by("-date")
        )

        # Aggregate new subscribers per day
        monthly_chart_data = (
            User.objects.annotate(date=TruncMonth("date_joined"))
            .values("date")
            .annotate(y=Count("id"))
            .order_by("-date")
        )

        # Serialize and attach the chart data to the template context
        as_json_daily = json.dumps(list(daily_chart_data), cls=DjangoJSONEncoder)
        as_json_weekly = json.dumps(list(weekly_chart_data), cls=DjangoJSONEncoder)
        as_json_monthly = json.dumps(list(monthly_chart_data), cls=DjangoJSONEncoder)
        extra_context = extra_context or {"daily_chart_data": as_json_daily, "weekly_chart_data": as_json_weekly, "monthly_chart_data": as_json_monthly}

        # Call the superclass changelist_view to render the page
        return super().changelist_view(request, extra_context=extra_context)