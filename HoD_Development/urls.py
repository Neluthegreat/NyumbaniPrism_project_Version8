from django.urls import path
from . import views

# This is important for namespacing your URLs
app_name = 'HoD_Development'

urlpatterns = [
    # The default view for the HoD will be the dashboard
    path('dashboard/', views.dashboard_view, name='dashboard'), 
    
    # Store & Inventory URLs
    path('store/', views.store_inventory_view, name='store_inventory'),
    path('store/catalog/', views.technical_asset_catalog_view, name='technical_asset_catalog'),
    path('store/asset/details/', views.detailed_asset_view, name='detailed_asset_view'),
    path('store/my-requisitions/', views.my_requisitions_view, name='my_requisitions'),

    # Customer Management URLs
    path('customers/', views.customer_management_view, name='customer_management'),
    path('customers/client-360/', views.client_360_view, name='client_360_view'),
    path('customers/health-dashboard/', views.client_health_dashboard_view, name='client_health_dashboard'),
    
    # Other Service Management URLs
    path('pipeline/', views.pipeline_view, name='pipeline'),
    path('projects/', views.projects_dashboard_view, name='projects_dashboard'),

    path('commercials/', views.commercials_view, name='commercials'),
    path('commercials/invoices/', views.invoices_view, name='invoices'),
    path('commercials/contracts/', views.contracts_view, name='contracts'),
    path('commercials/sows/', views.sows_view, name='sows'), # SOW = Statement of Work
    path('service-management/', views.service_management_view, name='service_management'),
    
    # The sub-pages within the module
    path('service-management/pipeline/', views.pipeline_view, name='pipeline'),
    path('service-management/projects-dashboard/', views.projects_dashboard_view, name='projects_dashboard'),
    path('service-management/support-queue/', views.support_queue_view, name='support_queue'),
    path('service-management/deployment-schedule/', views.deployment_schedule_view, name='deployment_schedule'),
]