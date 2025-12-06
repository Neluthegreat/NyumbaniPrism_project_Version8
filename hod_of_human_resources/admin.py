from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'department', 'position', 'status', 'hire_date']
    list_filter = ['department', 'status', 'hire_date']
    search_fields = ['first_name', 'last_name', 'email', 'department']
    date_hierarchy = 'hire_date'
