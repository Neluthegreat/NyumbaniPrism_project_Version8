# panel/admin.py

from django.contrib import admin
from django.apps import apps
from . import models

# --- Custom Admin Views ---

# This makes the user list more readable
@admin.register(models.Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'departmentid', 'roleid', 'status', 'is_staff')
    search_fields = ('username', 'email')
    list_filter = ('status', 'is_staff', 'departmentid', 'roleid')

# This makes the 'Customers' list much more useful
@admin.register(models.Customers)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customername', 'contactperson', 'email', 'status')
    search_fields = ('customername', 'contactperson', 'email')
    list_filter = ('status',)

# This makes the 'Projects' list more useful
@admin.register(models.Projects)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('projectname', 'customerid', 'status', 'startdate', 'enddate')
    search_fields = ('projectname',)
    list_filter = ('status',)


# --- Automatic Registration for All Other Models ---
# This part finds any model you haven't customized above and registers it.
app_models = apps.get_app_config('panel').get_models()
for model in app_models:
    if not admin.site.is_registered(model):
        admin.site.register(model)