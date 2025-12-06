# PRISM_PROJECT/Developer_staff/forms.py
from django import forms
from .models import Document, Project, Task, Sprint, TimeEntry
from django.contrib.auth import get_user_model

User = get_user_model()

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['name', 'project', 'file', 'version']
        # ... widgets ...

class TimeEntryForm(forms.ModelForm):
    duration_str = forms.CharField(label="Duration", help_text="Enter like '2h 30m'")
    class Meta:
        model = TimeEntry
        fields = ['project', 'task', 'date', 'notes']
        # ... widgets ...

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'project', 'sprint', 'assignee', 'status', 'priority', 'due_date', 'description']
        # ... widgets ...
    
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['sprint'].required = False
        self.fields['description'].required = False