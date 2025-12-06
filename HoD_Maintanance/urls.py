# HoD_Maintenance/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Main Dashboard
    path('', views.maintenance_dashboard, name='maintenance-dashboard'),
    
    # Service Management
    path('tickets/', views.ticketing_system_view, name='ticketing-system'),
    path('sla/', views.sla_management_view, name='sla-management'),
    path('changes/', views.change_management_view, name='change-management'),

    # Store & Inventory
    path('assets/', views.asset_management_view, name='asset-management'),
    path('history/', views.maintenance_history_view, name='maintenance-history'),
    path('requisitions/', views.inventory_requisitions_view, name='inventory-requisitions'),

    # Project Management
    path('contracts/', views.maintenance_contracts_view, name='maintenance-contracts'),
    path('visits/', views.scheduled_site_visits_view, name='scheduled-site-visits'),

    # Other
    path('analytics/', views.analytics_reporting_view, name='analytics-reporting'),
    path('settings/', views.system_settings_view, name='system-settings'),
]