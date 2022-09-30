from app.views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', home),
    path('<str:team_name>/', team_name),
    path('admin/', admin.site.urls),
]
