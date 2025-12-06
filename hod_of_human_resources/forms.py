from django import forms
from .models import (
    JobRequisition, HRPolicy, HRNotification, BudgetAdjustmentRequest,
    WorkforcePlan, Dispute, SuccessionPlan, Meeting
)

class JobRequisitionForm(forms.ModelForm):
    """Form for creating and editing job requisitions"""
    
    class Meta:
        model = JobRequisition
        fields = [
            'position', 'department', 'description', 'requirements',
            'salary_range', 'requested_by', 'status'
        ]
        
        widgets = {
            'position': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Job Position'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Job Description'}),
            'requirements': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Requirements'}),
            'salary_range': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 50000-70000'}),
            'requested_by': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

class HRPolicyForm(forms.ModelForm):
    """Form for creating and editing HR policies"""

    class Meta:
        model = HRPolicy
        fields = [
            'title', 'content', 'version', 'document', 'status', 'created_by'
        ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Policy Title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Policy Content'}),
            'version': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 1.0'}),
            'document': forms.FileInput(attrs={'class': 'form-control', 'accept': '.pdf'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'created_by': forms.Select(attrs={'class': 'form-control'}),
        }

class NotificationSettingsForm(forms.ModelForm):
    """Form for managing notification settings"""
    
    class Meta:
        model = HRNotification
        fields = [
            'title', 'message', 'notification_type', 'recipient', 'is_read'
        ]
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Notification Title'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Notification Message'}),
            'notification_type': forms.Select(attrs={'class': 'form-control'}),
            'recipient': forms.Select(attrs={'class': 'form-control'}),
            'is_read': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class BudgetAdjustmentRequestForm(forms.ModelForm):
    """Form for submitting budget adjustment requests"""
    
    class Meta:
        model = BudgetAdjustmentRequest
        fields = ['category', 'amount', 'reason']
        
        widgets = {
            'category': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Budget Category'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Adjustment Amount'}),
            'reason': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Reason for Adjustment'}),
        }

class LoginForm(forms.Form):
    """Form for HOD login"""
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        })
    )


class WorkforcePlanForm(forms.ModelForm):
    class Meta:
        model = WorkforcePlan
        fields = '__all__'
        widgets = {
            'department': forms.Select(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'headcount_needed': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }


class DisputeForm(forms.ModelForm):
    class Meta:
        model = Dispute
        fields = '__all__'
        widgets = {
            'employee': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }


class SuccessionPlanForm(forms.ModelForm):
    class Meta:
        model = SuccessionPlan
        fields = '__all__'
        widgets = {
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'employee': forms.Select(attrs={'class': 'form-control'}),
            'readiness': forms.Select(attrs={'class': 'form-control'}),
        }


class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ['title', 'purpose', 'venue', 'meeting_time', 'participants']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'purpose': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'venue': forms.TextInput(attrs={'class': 'form-control'}),
            'meeting_time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'participants': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
