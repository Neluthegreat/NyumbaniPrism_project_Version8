# graphicsmember/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# This is the function that your urls.py is looking for.
# The name must match EXACTLY: 'dashboard_view'
# @login_required # You can uncomment this later to make the page require a login
def dashboard_view(request):
    
    # This is placeholder data. In the future, you will get this from your database models.
    # For example: open_tasks = Task.objects.filter(assignee=request.user, status='Open')
    context = {
        'stats': {
            'total': 15,
            'in_progress': 6,
            'in_review': 3,
            'completed': 6
        },
        'open_tasks': [
            {'title': 'Animated Explainer', 'client': {'name': 'NMB Bank'}, 'due_date': '2025-08-15', 'status': 'New Requests', 'tag_color': 'var(--accent-green)', 'tag_color_light': 'rgba(22, 163, 74, 0.1)'},
            {'title': 'Brand Identity', 'client': {'name': 'Safari Adventures'}, 'due_date': '2025-08-20', 'status': 'In Progress', 'tag_color': 'var(--accent-blue)', 'tag_color_light': 'rgba(59, 130, 246, 0.1)'},
        ],
        'status_counts': [
            {'title': 'New Requests', 'count': 2, 'percentage': 20},
            {'title': 'In Progress', 'count': 6, 'percentage': 60},
            {'title': 'Review', 'count': 3, 'percentage': 30},
            {'title': 'Completed', 'count': 4, 'percentage': 40},
        ]
    }
    
    # This line tells Django to render the dashboard.html template
    # and pass the 'context' dictionary to it.
    return render(request, 'graphicsmember/dashboard.html', context)