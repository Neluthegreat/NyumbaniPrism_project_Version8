# memberofmaintenance/views.py

from django.shortcuts import render

# This view is already complete
def dashboard(request):
    return render(request, 'memberofmaintenance/dashboard.html')

# --- Add these new placeholder views ---

def ticket_system(request):
    return render(request, 'memberofmaintenance/tickets.html')

def scheduled_maintenance(request):
    return render(request, 'memberofmaintenance/schedule.html')

def knowledge_base(request):
    return render(request, 'memberofmaintenance/kb.html')

def asset_management(request):
    return render(request, 'memberofmaintenance/assets.html')

def inventory_requisition(request):
    return render(request, 'memberofmaintenance/requisition.html')

def maintenance_contracts(request):
    return render(request, 'memberofmaintenance/contracts.html')

def analytics_reporting(request):
    return render(request, 'memberofmaintenance/analytics.html')

def system_settings(request):
    return render(request, 'memberofmaintenance/settings.html')

def help_page(request):
    return render(request, 'memberofmaintenance/help.html')