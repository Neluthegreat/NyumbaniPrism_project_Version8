# memberofmaintenance/urls.py

from django.urls import path
from . import views

# This is important for namespacing your URLs
app_name = 'memberofmaintenance'

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # Service Management
    path('tickets/', views.ticket_system, name='ticket_system'),
    path('schedule/', views.scheduled_maintenance, name='scheduled_maintenance'),
    path('kb/', views.knowledge_base, name='knowledge_base'),

    # Store & Inventory
    path('assets/', views.asset_management, name='asset_management'),
    path('requisition/', views.inventory_requisition, name='inventory_requisition'),

    # Project Management
    path('contracts/', views.maintenance_contracts, name='maintenance_contracts'),
    
    # Other Links
    path('analytics/', views.analytics_reporting, name='analytics_reporting'),
    path('settings/', views.system_settings, name='system_settings'),
    path('help/', views.help_page, name='help_page'),
]