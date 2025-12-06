from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class HRDashboard(models.Model):
    """HR Dashboard model for tracking HR metrics and KPIs"""
    dashboard_id = models.AutoField(primary_key=True)
    department = models.ForeignKey('panel.Departments', on_delete=models.CASCADE, db_column='departmentid')
    total_headcount = models.IntegerField(default=0)
    open_requisitions = models.IntegerField(default=0)
    high_priority_cases = models.IntegerField(default=0)
    compliance_alerts = models.IntegerField(default=0)
    turnover_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    avg_hire_time = models.IntegerField(default=0)
    satisfaction_score = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    budget_utilization = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'hr_dashboard'

    def __str__(self):
        return f"HR Dashboard - {self.department.departmentname}"

class JobRequisition(models.Model):
    """Job requisition model for managing job postings"""
    REQUISITION_STATUS = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('filled', 'Filled'),
        ('cancelled', 'Cancelled'),
    ]

    requisition_id = models.AutoField(primary_key=True)
    position = models.CharField(max_length=255)
    department = models.ForeignKey('panel.Departments', on_delete=models.CASCADE, db_column='departmentid')
    description = models.TextField()
    requirements = models.TextField()
    salary_range = models.CharField(max_length=100)
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requested_requisitions', db_column='requested_by')
    status = models.CharField(max_length=20, choices=REQUISITION_STATUS, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'job_requisitions'

    def __str__(self):
        return f"{self.position} - {self.department.departmentname}"

class HRPolicy(models.Model):
    """HR Policy model for managing company policies"""
    POLICY_STATUS = [
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('archived', 'Archived'),
    ]

    policy_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    version = models.CharField(max_length=10)
    document = models.FileField(upload_to='hr_policies/', blank=True, null=True, help_text="Upload PDF document")
    status = models.CharField(max_length=20, choices=POLICY_STATUS, default='draft')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_policies', db_column='created_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'hr_policies'

    def __str__(self):
        return self.title

class HRNotification(models.Model):
    """HR Notification model for system notifications"""
    NOTIFICATION_TYPES = [
        ('requisition', 'Job Requisition'),
        ('policy', 'Policy Update'),
        ('compliance', 'Compliance Alert'),
        ('case', 'HR Case'),
        ('meeting', 'Meeting'),
    ]

    notification_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    message = models.TextField()
    notification_type = models.CharField(max_length=20, choices=NOTIFICATION_TYPES)
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hr_notifications', db_column='recipient', null=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'hr_notification'

    def __str__(self):
        return f"{self.title} - {self.recipient.username}"

# Keep the existing Employee model
class Employee(models.Model):
    """Employee model for HR management"""
    account_number = models.CharField(max_length=50, blank=True, null=True, help_text="Bank account number for payments")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2, help_text="Monthly base salary")
    allowance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, help_text="Monthly allowance amount")
    overtime = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, help_text="Current overtime amount")
    hire_date = models.DateField()
    status = models.CharField(max_length=20, choices=[
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('on_leave', 'On Leave'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def total_payable(self):
        """Calculate total amount payable (salary + allowance + overtime)"""
        return self.salary + self.allowance + self.overtime

class FinancialReport(models.Model):
    """Model to store generated financial reports"""
    report_id = models.AutoField(primary_key=True)
    generated_at = models.DateTimeField(auto_now_add=True)
    report_name = models.CharField(max_length=255)
    file_path = models.CharField(max_length=500, blank=True, null=True)  # Path to stored report file if applicable

    class Meta:
        managed = True
        db_table = 'financial_reports'

    def __str__(self):
        return f"{self.report_name} generated on {self.generated_at.strftime('%Y-%m-%d %H:%M:%S')}"

class BudgetAdjustmentRequest(models.Model):
    """Model to store budget adjustment requests"""
    REQUEST_STATUS = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    request_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    reason = models.TextField()
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='budget_adjustments')
    status = models.CharField(max_length=20, choices=REQUEST_STATUS, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'budget_adjustment_requests'

    def __str__(self):
        return f"Adjustment Request for {self.category} - {self.amount} by {self.requested_by.username}"


class Payment(models.Model):
    """Model to store payment transaction records"""
    PAYMENT_STATUS = [
        ('success', 'Success'),
        ('failed', 'Failed'),
        ('pending', 'Pending'),
    ]

    payment_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20, choices=PAYMENT_STATUS, default='pending')

    def __str__(self):
        return f"Payment of {self.amount} to {self.employee.full_name} on {self.payment_date.strftime('%Y-%m-%d')}"


class WorkforcePlan(models.Model):
    """Model for workforce planning"""
    plan_id = models.AutoField(primary_key=True)
    department = models.ForeignKey('panel.Departments', on_delete=models.CASCADE, db_column='departmentid')
    position = models.CharField(max_length=255)
    headcount_needed = models.IntegerField()
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'workforce_plans'

    def __str__(self):
        return f"Workforce Plan for {self.position} in {self.department.departmentname}"


class Dispute(models.Model):
    """Model for dispute resolution"""
    dispute_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='disputes')
    description = models.TextField()
    status = models.CharField(max_length=20, choices=[('open', 'Open'), ('closed', 'Closed')], default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'disputes'

    def __str__(self):
        return f"Dispute ID: {self.dispute_id} for {self.employee.full_name}"


class SuccessionPlan(models.Model):
    """Model for succession planning"""
    plan_id = models.AutoField(primary_key=True)
    position = models.CharField(max_length=255)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='succession_plans')
    readiness = models.CharField(max_length=20, choices=[('ready', 'Ready'), ('developing', 'Developing'), ('future', 'Future')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'succession_plans'

    def __str__(self):
        return f"Succession Plan for {self.position}"


class Meeting(models.Model):
    """Model for managing meetings"""
    meeting_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    purpose = models.TextField()
    venue = models.CharField(max_length=255)
    meeting_time = models.DateTimeField()
    participants = models.ManyToManyField(User, related_name='meetings')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_meetings')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'meetings'

    def __str__(self):
        return self.title
