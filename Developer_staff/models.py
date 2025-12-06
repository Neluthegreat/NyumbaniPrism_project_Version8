# PRISM_PROJECT/Developer_staff/models.py
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Project(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True, null=True)
    client_name = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self): return self.name

class Sprint(models.Model): # Example Sprint model, if you don't have one
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    def __str__(self):
        return self.name
class Ticket(models.Model):
    class Priority(models.TextChoices): LOW = 'LOW', 'Low'; MEDIUM = 'MEDIUM', 'Medium'; HIGH = 'HIGH', 'High'
    class Status(models.TextChoices): NEW = 'NEW', 'New'; OPEN = 'OPEN', 'Open'; IN_PROGRESS = 'IN_PROGRESS', 'In Progress'; PENDING_INFO = 'PENDING_INFO', 'Pending Info'; RESOLVED = 'RESOLVED', 'Resolved'; CLOSED = 'CLOSED', 'Closed'
    ticket_id = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tickets')
    priority = models.CharField(max_length=10, choices=Priority.choices, default=Priority.MEDIUM)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.NEW)
    reported_by = models.CharField(max_length=100)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='dev_staff_tickets')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self): return f"{self.ticket_id}: {self.title}"

class Task(models.Model):
    class Status(models.TextChoices): BACKLOG = 'BACKLOG', 'Backlog'; TODO = 'TODO', 'To Do'; IN_PROGRESS = 'IN_PROGRESS', 'In Progress'; IN_REVIEW = 'IN_REVIEW', 'In Review'; DONE = 'DONE', 'Done'
    class Priority(models.TextChoices): LOW = 'LOW', 'Low'; MEDIUM = 'MEDIUM', 'Medium'; HIGH = 'HIGH', 'High'
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    sprint = models.ForeignKey(Sprint, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.TODO)
    priority = models.CharField(max_length=10, choices=Priority.choices, default=Priority.MEDIUM)
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='dev_staff_tasks')
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self): return self.title

class Document(models.Model):
    name = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='documents')
    file = models.FileField(upload_to='project_documents/')
    version = models.CharField(max_length=20, blank=True)
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='modified_dev_documents')
    last_modified = models.DateTimeField(auto_now=True)
    def __str__(self): return self.name

class TimeEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dev_staff_time_entries')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()
    duration = models.DurationField()
    notes = models.TextField(blank=True)
    def __str__(self): return f"{self.user.username} - {self.duration} on {self.date}"
