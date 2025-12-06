from django.urls import path
from . import views

# This is a common practice to avoid name collisions with other apps
app_name = 'Developer_staff'

urlpatterns = [
    # A main dashboard or index view for the developer staff
    path('', views.dashboard_view, name='dashboard'),

    # URL for the Service Management / Ticketing Module
    path('tickets/', views.service_management_view, name='service_management'),

    # URL for Customer Management / Client Projects
    path('clients/', views.customer_management_view, name='customer_management'),

    # URL for the WBS & Sprints view
    path('wbs-sprints/', views.wbs_sprints_view, name='wbs_sprints'),

    # URL for the general Task Management view
    path('tasks/', views.task_management_view, name='task_management'),
    

    # URL for the Project Documentation view
    path('documentation/', views.documentation_view, name='documentation'),
    path('documentation/upload/', views.document_upload_view, name='document_upload'),

    # URL for the Time Tracking view
    path('time-tracking/', views.time_tracking_view, name='time_tracking'),
    path('time-tracking/log/', views.time_log_view, name='time_log'),

]