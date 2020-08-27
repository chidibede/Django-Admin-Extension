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
