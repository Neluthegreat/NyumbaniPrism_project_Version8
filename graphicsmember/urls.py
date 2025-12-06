# graphicsmember/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # This new path matches the empty string "" after /graphicsmember/
    # So it will now load the dashboard at http://127.0.0.1:8000/graphicsmember/
    path('', views.dashboard_view, name='dashboard'), 
]