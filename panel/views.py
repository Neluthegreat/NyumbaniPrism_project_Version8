from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse, HttpResponseBadRequest
from .models import Customers, Users, Roles, Departments
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Dashboard View
def dashboard_view(request):
    return render(request, 'Dashboard.html')

# Login View
def login_view(request):
    if request.method == 'POST':
        username_email = request.POST.get('username_email')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me') == 'on'

        # Try to authenticate using either username or email
        user = authenticate(request, username=username_email, password=password)
        if not user:
            # If authentication fails, try email-based lookup
            try:
                user = Users.objects.get(email=username_email)
                if check_password(password, user.password):
                    user = authenticate(request, username=user.username, password=password)
                else:
                    user = None
            except Users.DoesNotExist:
                user = None

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('dashboard.html')
        else:
            messages.error(request, "Invalid username/email or password.")
            return render(request, 'Login.html')

    return render(request, 'Login.html')

# Customer Management View
def customer_management_view(request):
    if request.method == 'POST':
        if 'delete_customer' in request.POST:
            customer_id = request.POST.get('customer_id')
            customer = get_object_or_404(Customers, pk=customer_id)
            customer.delete()
            messages.success(request, "Customer deleted successfully.")
            return redirect('customer-management')
        elif 'edit_customer' in request.POST:
            customer_id = request.POST.get('customer_id')
            customer = get_object_or_404(Customers, pk=customer_id)
            customer.customername = request.POST.get('customer_name')
            customer.contactperson = request.POST.get('contact_person')
            customer.email = request.POST.get('email')
            customer.phone = request.POST.get('phone')
            customer.status = request.POST.get('status')
            customer.save()
            messages.success(request, "Customer updated successfully.")
            return redirect('customer-management')
        elif 'add_customer' in request.POST:
            customer = Customers(
                customername=request.POST.get('customer_name'),
                contactperson=request.POST.get('contact_person'),
                email=request.POST.get('email'),
                phone=request.POST.get('phone'),
                status=request.POST.get('status')
            )
            customer.save()
            messages.success(request, "Customer added successfully.")
            return redirect('customer-management')

    all_customers = Customers.objects.all()
    context = {
        'customers': all_customers,
        'total_customers': all_customers.count(),
        'active_accounts': all_customers.filter(status='Active').count(),
        'new_this_month': all_customers.filter(createdat__month=8, createdat__year=2025).count(),
        'inactive_accounts': all_customers.filter(status='Inactive').count(),
    }
    return render(request, 'Customer Management.html', context)

# System Settings View
def system_settings_view(request):
    if request.method == 'POST':
        if 'delete_user' in request.POST:
            user_id = request.POST.get('user_id')
            user = get_object_or_404(Users, pk=user_id)
            user.delete()
            messages.success(request, "User deleted successfully.")
            return redirect('system-settings')
        elif 'edit_user' in request.POST:
            user_id = request.POST.get('user_id')
            user = get_object_or_404(Users, pk=user_id)
            user.username = request.POST.get('username')
            user.email = request.POST.get('email')
            password = request.POST.get('password')
            if password:
                user.password = make_password(password)
            try:
                role_id = request.POST.get('role')
                user.roleid_id = get_object_or_404(Roles, pk=role_id).roleid if role_id else None
                department_id = request.POST.get('department')
                user.departmentid_id = get_object_or_404(Departments, pk=department_id).departmentid if department_id else None
                user.status = request.POST.get('status')
                user.save()
                messages.success(request, "User updated successfully.")
            except ObjectDoesNotExist:
                messages.error(request, "Invalid role or department selected.")
                return render(request, 'System Settings.html', {
                    'users': Users.objects.select_related('roleid', 'departmentid').all(),
                    'roles': Roles.objects.all(),
                    'departments': Departments.objects.all(),
                })
            return redirect('system-settings')
        elif 'add_user' in request.POST:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            role_id = request.POST.get('role')
            department_id = request.POST.get('department')
            status = request.POST.get('status')

            if not all([username, email, password, role_id, status]):
                messages.error(request, "All required fields (username, email, password, role, status) are mandatory.")
                return render(request, 'System Settings.html', {
                    'users': Users.objects.select_related('roleid', 'departmentid').all(),
                    'roles': Roles.objects.all(),
                    'departments': Departments.objects.all(),
                })

            try:
                if Users.objects.filter(username=username).exists() or Users.objects.filter(email=email).exists():
                    messages.error(request, "Username or email already exists.")
                    return render(request, 'System Settings.html', {
                        'users': Users.objects.select_related('roleid', 'departmentid').all(),
                        'roles': Roles.objects.all(),
                        'departments': Departments.objects.all(),
                    })

                role_obj = get_object_or_404(Roles, pk=role_id)
                department_obj = get_object_or_404(Departments, pk=department_id) if department_id else None
                hashed_password = make_password(password)
                new_user = Users(
                    username=username,
                    email=email,
                    password=hashed_password,
                    roleid=role_obj,
                    departmentid=department_obj,
                    status=status
                )
                new_user.save()
                messages.success(request, "User added successfully.")
            except ObjectDoesNotExist:
                messages.error(request, "Invalid role or department selected.")
            except Exception as e:
                messages.error(request, f"An error occurred: {str(e)}")
            return redirect('system-settings')
        elif 'add_role' in request.POST:
            role_name = request.POST.get('role_name')
            description = request.POST.get('description')

            if not role_name:
                messages.error(request, "Role name is required.")
                return render(request, 'System Settings.html', {
                    'users': Users.objects.select_related('roleid', 'departmentid').all(),
                    'roles': Roles.objects.all(),
                    'departments': Departments.objects.all(),
                })

            try:
                if Roles.objects.filter(rolename=role_name).exists():
                    messages.error(request, "Role name already exists.")
                    return render(request, 'System Settings.html', {
                        'users': Users.objects.select_related('roleid', 'departmentid').all(),
                        'roles': Roles.objects.all(),
                        'departments': Departments.objects.all(),
                    })

                new_role = Roles(
                    rolename=role_name,
                    description=description or ""
                )
                new_role.save()
                messages.success(request, "Role added successfully.")
            except Exception as e:
                messages.error(request, f"An error occurred: {str(e)}")
            return redirect('system-settings')

    user_list = Users.objects.select_related('roleid', 'departmentid').all()
    all_roles = Roles.objects.all()
    all_departments = Departments.objects.all()
    context = {
        'users': user_list,
        'roles': all_roles,
        'departments': all_departments,
    }
    return render(request, 'System Settings.html', context)