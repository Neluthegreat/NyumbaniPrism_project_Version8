from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Each function corresponds to a specific page/module.

def dashboard_view(request):
    """Renders the main Service Management dashboard."""
    return render(request, 'HoD_Development/dashboard.html')

def store_inventory_view(request):
    """Renders the Store & Inventory landing page."""
    return render(request, 'HoD_Development/store_inventory.html')

def technical_asset_catalog_view(request):
    """Renders the browseable asset catalog."""
    return render(request, 'HoD_Development/technical_asset_catalog.html')

def detailed_asset_view(request):
    """Renders the detailed view for a single asset."""
    return render(request, 'HoD_Development/detailed_asset_view.html')

def my_requisitions_view(request):
    """Renders the user's list of asset requisitions."""
    return render(request, 'HoD_Development/my_requisitions.html')

def customer_management_view(request):
    """Renders the customer management overview."""
    return render(request, 'HoD_Development/customer_management.html')

def client_360_view(request):
    """Renders the detailed 360 view for a single client."""
    return render(request, 'HoD_Development/client_360_view.html')

def client_health_dashboard_view(request):
    """Renders the client health analytics dashboard."""
    return render(request, 'HoD_Development/client_health_dashboard.html')

# Add other views for pipeline, projects, support, etc. following the same pattern.
# For example:
def pipeline_view(request):
    """Renders the project pipeline view."""
    return render(request, 'HoD_Development/pipeline.html')

def projects_dashboard_view(request):
    """Renders the active projects dashboard."""
    return render(request, 'HoD_Development/projects_dashboard.html')

# ... (existing imports) ...

# --- ADD THESE NEW COMMERCIALS VIEWS ---

def commercials_view(request: HttpRequest) -> HttpResponse:
    """Renders the main landing page for the Commercials module."""
    # You can pass context data here in the future
    return render(request, 'HoD_Development/commercials.html')

def invoices_view(request: HttpRequest) -> HttpResponse:
    """Renders the Invoices page."""
    return render(request, 'HoD_Development/invoices.html')

def contracts_view(request: HttpRequest) -> HttpResponse:
    """Renders the Contracts page."""
    return render(request, 'HoD_Development/contracts.html')

def sows_view(request: HttpRequest) -> HttpResponse:
    """Renders the Statements of Work (SOWs) page."""
    return render(request, 'HoD_Development/sows.html')


# ... (all your other existing view functions) ...
def service_management_view(request: HttpRequest) -> HttpResponse:
    """Renders the main landing page for the Service Management module."""
    # This view no longer needs to pass data, just render the navigation page.
    return render(request, 'HoD_Development/service_management.html')

# --- KEEP these sub-page views ---
def pipeline_view(request: HttpRequest) -> HttpResponse:
    """Renders the Project Pipeline page."""
    # In a real app, you would add context data here for the pipeline table
    return render(request, 'HoD_Development/pipeline.html')

def projects_dashboard_view(request: HttpRequest) -> HttpResponse:
    """Renders the Active Projects Dashboard page."""
    # In a real app, you would add context data here for project cards
    return render(request, 'HoD_Development/projects_dashboard.html')

def support_queue_view(request: HttpRequest) -> HttpResponse:
    """Renders the Support & Maintenance Queue page."""
    # In a real app, you would add context data here for the tickets table
    return render(request, 'HoD_Development/support_queue.html')

def deployment_schedule_view(request: HttpRequest) -> HttpResponse:
    """Renders the Deployment Schedule page."""
    return render(request, 'HoD_Development/deployment_schedule.html')