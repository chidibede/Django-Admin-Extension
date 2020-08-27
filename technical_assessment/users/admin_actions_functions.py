from django.contrib import messages
from django.utils.translation import ngettext
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

def set_active(modeladmin, request, queryset):
    updated = queryset.update(is_active=True)
    modeladmin.message_user(request, ngettext(
            '%d user was successfully activated.',
            '%d users were successfully activated.',
            updated,
        ) % updated, messages.SUCCESS)

set_active.short_description = 'Activate selected Users'

def set_inactive(modeladmin, request, queryset):
    updated = queryset.update(is_active=False)
    modeladmin.message_user(request, ngettext(
            '%d user was successfully deactivated.',
            '%d users were successfully deactivated.',
            updated,
        ) % updated, messages.SUCCESS)

set_inactive.short_description = 'Deactivate selected Users'


def set_staff_status(modeladmin, request, queryset):
    updated = queryset.update(is_staff=True)
    modeladmin.message_user(request, ngettext(
            '%d user was successfully authorized as staff.',
            '%d users were successfully authorized as staff.',
            updated,
        ) % updated, messages.SUCCESS)

set_staff_status.short_description = 'Authorize as Staff'


def remove_staff_status(modeladmin, request, queryset):
    updated = queryset.update(is_staff=False)
    modeladmin.message_user(request, ngettext(
            '%d user was successfully removed as staff.',
            '%d users were successfully removed as staff.',
            updated,
        ) % updated, messages.SUCCESS)

remove_staff_status.short_description = 'Remove as staff'