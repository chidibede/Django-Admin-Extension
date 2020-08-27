from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='pages-home'),
     path('admin_login/', views.admin_login, name='admin-login'),
]
