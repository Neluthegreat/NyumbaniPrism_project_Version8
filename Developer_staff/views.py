# PRISM_PROJECT/Developer_staff/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone as tz
from django.urls import reverse
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from datetime import timedelta, date
import re

# THE FIX: Only models are imported at the top level.
from .models import Project, Ticket, Task, Document, TimeEntry, Sprint

# This helper function is needed.
def parse_duration(duration_str):
    if not duration_str: return None
    parts = re.findall(r'(\d+)\s*(h|m)', duration_str.lower())
    if not parts: return None
    duration = timedelta()
    for value, unit in parts:
        value = int(value)
        if unit == 'h': duration += timedelta(hours=value)
        elif unit == 'm': duration += timedelta(minutes=value)
    return duration

# --- ALL VIEWS ARE PRESENT BELOW ---

@login_required
def dashboard_view(request):
    user = request.user
    active_tickets_count = Ticket.objects.filter(assigned_to=user).exclude(status__in=['RESOLVED', 'CLOSED']).count()
    tasks_in_progress_count = Task.objects.filter(assignee=user, status='IN_PROGRESS').count()
    overdue_tasks_count = Task.objects.filter(assignee=user, due_date__lt=tz.now().date()).exclude(status='DONE').count()
    context = {
        'active_tickets_count': active_tickets_count,
        'tasks_in_progress_count': tasks_in_progress_count,
        'overdue_tasks_count': overdue_tasks_count,
        'user': user
    }
    return render(request, 'Developer_staff/dashboard.html', context)

@login_required
def service_management_view(request):
    # This view was missing
    tickets_list = Ticket.objects.filter(assigned_to=request.user).select_related('project').order_by('-updated_at')
    context = {
        'tickets': tickets_list,
        'projects': Project.objects.all(),
        'ticket_statuses': Ticket.Status.choices,
        'ticket_priorities': Ticket.Priority.choices,
        'current_filters': {}
    }
    return render(request, 'Developer_staff/service_management.html', context)

@login_required
def customer_management_view(request):
    # This view was missing
    user_projects = Project.objects.filter(tasks__assignee=request.user).distinct()
    context = {'projects': user_projects}
    return render(request, 'Developer_staff/customer_management.html', context)

@login_required
def wbs_sprints_view(request):
    # This view was missing
    all_projects = Project.objects.all()
    selected_project = None
    sprints = []
    tasks_by_status = {}
    project_id = request.GET.get('project')
    if project_id:
        try:
            selected_project = Project.objects.get(id=project_id)
            sprints = Sprint.objects.filter(project=selected_project).order_by('start_date')
            tasks = Task.objects.filter(project=selected_project)
            tasks_by_status = {
                'backlog': tasks.filter(status='BACKLOG'), 'todo': tasks.filter(status='TODO'),
                'in_progress': tasks.filter(status='IN_PROGRESS'), 'in_review': tasks.filter(status='IN_REVIEW'),
                'done': tasks.filter(status='DONE'),
            }
        except Project.DoesNotExist:
            selected_project = None
    context = {
        'all_projects': all_projects, 'selected_project': selected_project,
        'sprints': sprints, 'tasks_by_status': tasks_by_status,
    }
    return render(request, 'Developer_staff/wbs_sprints.html', context)

@login_required
def task_management_view(request):
    # This view was missing
    my_tasks = Task.objects.filter(assignee=request.user)
    context = {'tasks': my_tasks}
    return render(request, 'Developer_staff/task_management.html', context)

@login_required
def documentation_view(request):
    # This view was missing
    documents = Document.objects.all().order_by('-last_modified')
    for doc in documents:
        name_lower = doc.name.lower()
        if name_lower.endswith('.pdf'): doc.file_type = 'pdf'
        elif name_lower.endswith(('.docx', '.doc')): doc.file_type = 'word'
        elif name_lower.endswith(('.png', '.jpg', '.jpeg')): doc.file_type = 'image'
        else: doc.file_type = 'other'
    context = {'documents': documents}
    return render(request, 'Developer_staff/documentation.html', context)

@login_required
def time_tracking_view(request):
    # This view was missing
    user = request.user
    time_entries = TimeEntry.objects.filter(user=user).order_by('-date')
    today = date.today()
    start_of_week = today - timedelta(days=today.weekday())
    entries_today = time_entries.filter(date=today)
    total_duration_today = sum([entry.duration for entry in entries_today], timedelta())
    entries_this_week = time_entries.filter(date__gte=start_of_week)
    total_duration_this_week = sum([entry.duration for entry in entries_this_week], timedelta())
    context = {
        'time_entries': time_entries,
        'duration_today': total_duration_today,
        'duration_this_week': total_duration_this_week,
        'overdue_days': 2,
    }
    return render(request, 'Developer_staff/time_tracking.html', context)

# --- Views with Forms (Local Imports) ---

@login_required
def document_upload_view(request):
    from .forms import DocumentForm
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.modified_by = request.user
            document.save()
            return redirect('Developer_staff:documentation')
    else:
        form = DocumentForm()
    return render(request, 'Developer_staff/document_upload.html', {'form': form})

@login_required
def time_log_view(request):
    from .forms import TimeEntryForm
    user = request.user
    project_queryset = Project.objects.filter(tasks__assignee=user).distinct()
    task_queryset = Task.objects.filter(assignee=user)
    if request.method == 'POST':
        form = TimeEntryForm(request.POST)
        form.fields['project'].queryset = project_queryset
        form.fields['task'].queryset = task_queryset
        duration = parse_duration(request.POST.get('duration_str'))
        if form.is_valid() and duration:
            entry = form.save(commit=False)
            entry.user = user
            entry.duration = duration
            entry.save()
            return redirect('Developer_staff:time_tracking')
        else:
            if not duration: form.add_error('duration_str', 'Invalid format.')
    else:
        form = TimeEntryForm()
        form.fields['project'].queryset = project_queryset
        form.fields['task'].queryset = task_queryset
    return render(request, 'Developer_staff/log_time.html', {'form': form})

# (Placeholder for task CRUD views, which can be added back later)