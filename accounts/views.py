from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
from django.middleware.csrf import get_token
from django.utils.http import url_has_allowed_host_and_scheme
from django.conf import settings
from panel.models import Orders, Inventory, Users

import logging

logger = logging.getLogger(__name__)

def home_view(request):
    """Home page view - always redirects to login page"""
    return redirect('accounts:login')  # Always redirect to login page

@ensure_csrf_cookie
def login_view(request):
    """Login view with role-based redirection and proper CSRF protection"""
    # Ensure CSRF token is generated and cookie is set
    if request.method == 'GET':
        get_token(request)
        logger.debug("CSRF token generated for GET request")
    
    # This view will handle both displaying the login form and processing the submission
    if request.method == 'POST':
        # Debug CSRF information
        csrf_token_post = request.POST.get('csrfmiddlewaretoken')
        csrf_token_cookie = request.COOKIES.get('csrftoken')
        
        logger.debug("CSRF Token from POST: %s", csrf_token_post)
        logger.debug("CSRF Token from cookies: %s", csrf_token_cookie)
        logger.debug("Session ID: %s", request.session.session_key)
        logger.debug("All POST data: %s", dict(request.POST))
        logger.debug("All cookies: %s", dict(request.COOKIES))
        
        # Validate CSRF token before proceeding
        if not csrf_token_post:
            logger.error("CSRF token missing from POST data")
            messages.error(request, 'CSRF token is missing. Please refresh the page and try again.')
            return render(request, 'accounts/Login.html')
        
        if not csrf_token_cookie:
            logger.error("CSRF token missing from cookies")
            messages.error(request, 'CSRF token cookie is missing. Please enable cookies and try again.')
            return render(request, 'accounts/Login.html')
        
        username_or_email = request.POST.get('username')
        password = request.POST.get('password')
        
        logger.debug("Login attempt with username/email: %s", username_or_email)
        
        # Since USERNAME_FIELD is 'email' in our custom user model,
        # we need to determine if the input is an email or username
        from panel.models import Users
        
        user = None
        try:
            # First, try to find the user by email
            user_obj = Users.objects.get(email=username_or_email)
            # Authenticate using the email (which is the USERNAME_FIELD)
            user = authenticate(request, username=user_obj.email, password=password)
        except Users.DoesNotExist:
            try:
                # If not found by email, try to find by username
                user_obj = Users.objects.get(username=username_or_email)
                # Authenticate using the email (which is the USERNAME_FIELD)
                user = authenticate(request, username=user_obj.email, password=password)
            except Users.DoesNotExist:
                user = None
        
        logger.debug("Authentication result: %s", user is not None)
        
        if user is not None:
            logger.info("User %s authenticated successfully.", username_or_email)
            # No welcome message - just login and redirect
            login(request, user)
            
            # If there is a valid next parameter, honor it first to avoid loops
            next_url = request.POST.get('next') or request.GET.get('next')
            if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
                return redirect(next_url)

            # Redirect users to their respective dashboards based on their role
            if user.roleid:
                role_name = (user.roleid.rolename or '').strip().lower()
                logger.debug("User role: %s", role_name)

                # Graphics roles
                if 'graphics' in role_name and ('head' in role_name or 'hod' in role_name):
                    # Head of Graphics
                    return redirect('headofgraphics:hod_dashboard')
                elif 'graphics' in role_name and (
                    'member' in role_name or 'employee' in role_name or 'staff' in role_name
                ):
                    # Graphics team member
                    return redirect('graphicsmember:dashboard')
                elif 'human resources' in role_name or 'hr' in role_name:
                    # Redirect to HOD Human Resources dashboard
                    return redirect('hod_of_human_resources:hod_dashboard')
                elif 'admin' in role_name or 'administrator' in role_name or 'system admin' in role_name.lower():
                    # Redirect to system admin dashboard
                    return redirect('system_admin:dashboard')
                elif 'marketing' in role_name and ('head' in role_name or 'hod' in role_name):
                    # Redirect to Head of Marketing dashboard
                    return redirect('headofmarketing:dashboard')
                elif 'printing' in role_name and ('head' in role_name or 'hod' in role_name):
                    # Redirect to Head of Printing dashboard
                    return redirect('hod_printing:dashboard')
                elif 'chief accountant' in role_name.lower():
                    # Redirect to Chief Accountant dashboard
                    return redirect('chiefaccountant:dashboard')
                elif 'headofmaintenance' in role_name.lower() or 'head of maintenance' in role_name.lower() or 'maintenance head' in role_name.lower():
                    # Redirect to Head of Maintenance dashboard
                    return redirect('headofmaintenance:maintenance-dashboard')
                elif 'memberofmaintenance' in role_name or 'employee' in role_name or 'maintenance member' in role_name:
                    # Redirect to Maintenance Member dashboard
                    return redirect('memberofmaintenance:dashboard')
                elif 'printing' in role_name and 'member' in role_name:
                    # Redirect to Printing Member dashboard
                    return redirect('printing_staff:dashboard')
                elif 'resource seller' in role_name.lower():
                    # Redirect to Resource Seller dashboard
                    return redirect('headofresourceselling:dashboard')
                elif 'inventory manager' in role_name.lower():
                    # Redirect to Inventory Manager dashboard
                    return redirect('inventorymanager:dashboard')
                elif 'managing director' in role_name.lower():
                    # Redirect to Managing Director dashboard
                    return redirect('managingdirector:dashboard')
                elif 'system development' in role_name.lower() or 'development head' in role_name.lower():
                    # Redirect to Head of System Development dashboard
                    return redirect('HoD_Development:dashboard')
                elif 'system developer' in role_name.lower():
                    # Redirect to System Developer dashboard
                    return redirect('systemdeveloper:dashboard')
                else:
                    # For other roles, try to determine based on role name
                    if 'hod' in role_name or 'head' in role_name:
                        # If it's a head of department role, redirect to panel dashboard
                        return redirect('panel:panel_dashboard')
                    else:
                        # Default redirect for other roles
                        return redirect('panel:panel_dashboard')
            else:
                # No role assigned, redirect to general panel dashboard
                logger.warning("User %s has no role assigned, redirecting to panel dashboard", user.username)
                return redirect('panel:panel_dashboard')
        else:
            logger.warning("Failed login attempt for username/email: %s", username_or_email)
            messages.error(request, 'Invalid username/email or password.')
            
    # For a GET request or a failed POST, render the login page again.
    return render(request, 'accounts/Login.html')

@login_required
def logout_view(request):
    """Logout view"""
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('accounts:login')

@login_required
def profile_view(request):
    """User profile view"""
    return render(request, 'accounts/profile.html')

@login_required
def settings_view(request):
    """User settings view"""
    return render(request, 'accounts/settings.html')
