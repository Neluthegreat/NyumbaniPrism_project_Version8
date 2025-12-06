from django.db import models
from django.conf import settings

class UserProfile(models.Model):
    """Extended user profile for PRISM system"""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=[
        ('admin', 'Admin'),
        ('hod_graphics', 'Head of Graphics'),
        ('hod_human_resources', 'Head of Human Resources'),
        ('head_of_department', 'Head of Department'),
        ('staff', 'Staff'),
        ('system_developer', 'System Developer'),
    ])
    department = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.role}"
