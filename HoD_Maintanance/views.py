from django.shortcuts import render

# ================== Main Dashboard View ==================
def maintenance_dashboard(request):
    """
    Renders the main dashboard page.
    """
    return render(request, 'HoD_Maintenance/dashboard.html')

# ================== Service Management Views ==================
def ticketing_system_view(request):
    """
    Renders the ticketing system page.
    """
    return render(request, 'HoD_Maintenance/ticketing.html')

def sla_management_view(request):
    """
    Renders the SLA management page.
    """
    return render(request, 'HoD_Maintenance/sla_management.html')

def change_management_view(request):
    """
    Renders the change management page.
    """
    return render(request, 'HoD_Maintenance/change_management.html')

# ================== Store & Inventory Views ==================
def asset_management_view(request):
    """
    Renders the asset management page.
    """
    return render(request, 'HoD_Maintenance/asset_management.html')

def maintenance_history_view(request):
    """
    Renders the maintenance history page.
    """
    return render(request, 'HoD_Maintenance/maintenance_history.html')

def inventory_requisitions_view(request):
    """
    Renders the inventory requisitions page.
    """
    return render(request, 'HoD_Maintenance/inventory_requisitions.html')

# ================== Project Management Views ==================
def maintenance_contracts_view(request):
    """
    Renders the maintenance contracts page.
    """
    return render(request, 'HoD_Maintenance/maintenance_contracts.html')

def scheduled_site_visits_view(request):
    """
    Renders the scheduled site visits page.
    """
    return render(request, 'HoD_Maintenance/scheduled_site_visits.html')

# ================== Other Views ==================
def analytics_reporting_view(request):
    """
    Renders the analytics and reporting page.
    """
    return render(request, 'HoD_Maintenance/analytics_reporting.html')

def system_settings_view(request):
    """
    Renders the system settings page.
    """
    return render(request, 'HoD_Maintenance/system_settings.html')