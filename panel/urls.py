from django.urls import path
from . import views

app_name = 'panel'

urlpatterns = [
    #path('', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='panel_dashboard'),
    path('customer-management/', views.customer_management_view, name='customer-management'),
    path('system-settings/', views.system_settings_view, name='system-settings'),
]
