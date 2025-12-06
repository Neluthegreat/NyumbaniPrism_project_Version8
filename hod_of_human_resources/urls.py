from django.urls import path
from . import views

app_name = 'hod_of_human_resources'

urlpatterns = [
    # Main views
    path('', views.dashboard, name='hod_dashboard'),
    path('financials/payments/', views.payment_page, name='payment_page'),
    path('financials/payments/<int:employee_id>/process/', views.process_payment, name='process_payment'),
    path('hr-management/', views.hr_management, name='hr_management'),
    path('analytics/', views.analytics, name='analytics'),
    path('financials/', views.financials, name='financials'),
    path('financials/generate-report/', views.generate_financial_report, name='generate_financial_report'),
    path('financials/export-payment-report/pdf/', views.export_payment_report_pdf, name='export_payment_report_pdf'),
    path('financials/export-payment-report/excel/', views.export_payment_report_excel, name='export_payment_report_excel'),
    path('financials/request-adjustment/', views.request_budget_adjustment, name='request_budget_adjustment'),
    path('settings/', views.settings, name='settings'),
    path('help/', views.help_support, name='help'),
    
    # API endpoints
    path('api/requisitions/', views.api_requisitions, name='api_requisitions'),
    
    # Requisition management
    path('requisitions/create/', views.create_requisition, name='create_requisition'),
    path('requisitions/<int:requisition_id>/update/', views.requisition_update, name='requisition_update'),
    path('requisitions/<int:requisition_id>/delete/', views.requisition_delete, name='requisition_delete'),
    path('requisitions/<int:requisition_id>/approve/', views.approve_requisition, name='approve_requisition'),
    path('requisitions/<int:requisition_id>/reject/', views.reject_requisition, name='reject_requisition'),
    
    # Policy management
    path('policies/create/', views.manage_policy, name='create_policy'),
    path('policies/<int:policy_id>/view/', views.view_policy, name='view_policy'),
    path('policies/<int:policy_id>/edit/', views.manage_policy, name='edit_policy'),

    # Workforce Planning
    path('workforce-plans/', views.workforce_plan_list, name='workforce_plan_list'),
    path('workforce-plans/create/', views.workforce_plan_create, name='workforce_plan_create'),
    path('workforce-plans/<int:pk>/update/', views.workforce_plan_update, name='workforce_plan_update'),
    path('workforce-plans/<int:pk>/delete/', views.workforce_plan_delete, name='workforce_plan_delete'),

    # Dispute Resolution
    path('disputes/', views.dispute_list, name='dispute_list'),
    path('disputes/create/', views.dispute_create, name='dispute_create'),
    path('disputes/<int:pk>/update/', views.dispute_update, name='dispute_update'),
    path('disputes/<int:pk>/delete/', views.dispute_delete, name='dispute_delete'),

    # Succession Planning
    path('succession-plans/', views.succession_plan_list, name='succession_plan_list'),
    path('succession-plans/create/', views.succession_plan_create, name='succession_plan_create'),
    path('succession-plans/<int:pk>/update/', views.succession_plan_update, name='succession_plan_update'),
    path('succession-plans/<int:pk>/delete/', views.succession_plan_delete, name='succession_plan_delete'),

    # Meeting Management
    path('meetings/', views.meeting_list, name='meeting_list'),
    path('meetings/create/', views.meeting_create, name='meeting_create'),
    path('meetings/<int:pk>/', views.meeting_detail, name='meeting_detail'),
    path('meetings/<int:pk>/update/', views.meeting_update, name='meeting_update'),
    path('meetings/<int:pk>/delete/', views.meeting_delete, name='meeting_delete'),
]
