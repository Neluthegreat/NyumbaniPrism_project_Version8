from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings # For linking to the User model correctly

# ==============================================================================
# ENUMERATIONS / CHOICES
# ==============================================================================
# Using classes for choices makes the code cleaner and less error-prone.

class ProjectHealth(models.TextChoices):
    ON_TRACK = 'ON_TRACK', 'On Track'
    AT_RISK = 'AT_RISK', 'At Risk'
    OFF_TRACK = 'OFF_TRACK', 'Off Track'

class TicketStatus(models.TextChoices):
    OPEN = 'OPEN', 'Open'
    IN_PROGRESS = 'IN_PROGRESS', 'In Progress'
    CLOSED = 'CLOSED', 'Closed'
    UNASSIGNED = 'UNASSIGNED', 'Unassigned'

class TicketPriority(models.TextChoices):
    HIGH = 'HIGH', 'High'
    MEDIUM = 'MEDIUM', 'Medium'
    LOW = 'LOW', 'Low'

class DeploymentStatus(models.TextChoices):
    SCHEDULED = 'SCHEDULED', 'Scheduled'
    IN_PROGRESS = 'IN_PROGRESS', 'In Progress'
    COMPLETED = 'COMPLETED', 'Completed'
    ROLLED_BACK = 'ROLLED_BACK', 'Rolled Back'

class RequisitionStatus(models.TextChoices):
    PENDING = 'PENDING', 'Pending'
    APPROVED = 'APPROVED', 'Approved'
    DENIED = 'DENIED', 'Denied'
    FULFILLED = 'FULFILLED', 'Fulfilled'

# ==============================================================================
# CORE MODELS
# ==============================================================================

class Client(models.Model):
    """Represents a client company."""
    name = models.CharField(max_length=200, unique=True, help_text="The official name of the client company.")
    primary_technical_contact_name = models.CharField(max_length=150, blank=True)
    account_manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='managed_clients')
    contract_start_date = models.DateField(null=True, blank=True)
    contract_end_date = models.DateField(null=True, blank=True)
    health_score = models.IntegerField(default=100, help_text="A score from 0 to 100 indicating client health.")

    def __str__(self):
        return self.name

class Project(models.Model):
    """Represents an active project being worked on for a client."""
    name = models.CharField(max_length=200)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='projects')
    team_lead = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='led_projects')
    team_members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='projects', blank=True)
    health = models.CharField(max_length=20, choices=ProjectHealth.choices, default=ProjectHealth.ON_TRACK)
    progress_percentage = models.IntegerField(default=0)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    actual_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    next_milestone_name = models.CharField(max_length=255, blank=True)
    next_milestone_due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.client.name})"

class Opportunity(models.Model):
    """Represents a potential project in the sales pipeline before it becomes a real project."""
    name = models.CharField(max_length=200)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='opportunities')
    sales_contact = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='opportunities')
    estimated_value = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, default="Awaiting Technical Assessment")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Opportunities"

    def __str__(self):
        return f"Opportunity: {self.name} for {self.client.name}"

class Ticket(models.Model):
    """Represents a single support or maintenance ticket."""
    subject = models.CharField(max_length=255)
    description = models.TextField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='tickets')
    submitted_by_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='submitted_tickets')
    status = models.CharField(max_length=20, choices=TicketStatus.choices, default=TicketStatus.UNASSIGNED)
    priority = models.CharField(max_length=20, choices=TicketPriority.choices, default=TicketPriority.MEDIUM)
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_tickets')
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"TICKET-{self.id}: {self.subject}"

class Deployment(models.Model):
    """Represents a scheduled software deployment for a project."""
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='deployments')
    deployment_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=DeploymentStatus.choices, default=DeploymentStatus.SCHEDULED)
    lead_developer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='led_deployments')
    change_request_id = models.CharField(max_length=50, blank=True, help_text="e.g., CR-12345")
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Deployment for {self.project.name} on {self.deployment_date.strftime('%Y-%m-%d')}"

# In HoD_Development/models.py

class AssetRequisition(models.Model):
    # ... other fields
    # This related_name should be unique. 'hod_asset_requisitions' is perfect.
    requester = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='hod_asset_requisitions' # <-- CONFIRM THIS IS SAVED
    )
    # ... other fields
class Contract(models.Model):
    """Represents a master service agreement or other contract with a client."""
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='contracts')
    title = models.CharField(max_length=255, default="Master Service Agreement")
    document_url = models.URLField(blank=True, help_text="Link to the signed document in cloud storage.")
    effective_date = models.DateField()
    expiration_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Contract for {self.client.name} ({self.effective_date.year})"