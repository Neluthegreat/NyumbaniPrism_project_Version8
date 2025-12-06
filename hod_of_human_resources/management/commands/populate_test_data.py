from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils import timezone
from hod_of_human_resources.models import (
    Employee, Payment, JobRequisition, HRPolicy, HRNotification,
    FinancialReport, BudgetAdjustmentRequest, HRDashboard
)
from panel.models import Departments, Users, Roles
from accounts.models import UserProfile
from decimal import Decimal
import random
from datetime import date, timedelta

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate test data for hod_of_human_resources app'

    def handle(self, *args, **options):
        self.stdout.write('Starting to populate test data...')

        # Ensure we have required related data
        self.create_related_data()

        # Create test employees
        self.create_employees()

        # Create payments
        self.create_payments()

        # Create job requisitions
        self.create_job_requisitions()

        # Create HR policies
        self.create_hr_policies()

        # Create HR notifications
        self.create_hr_notifications()

        # Create financial reports
        self.create_financial_reports()

        # Create budget adjustment requests
        self.create_budget_adjustments()

        # Create HR dashboard data
        self.create_hr_dashboard()

        self.stdout.write(self.style.SUCCESS('Successfully populated test data!'))

    def create_related_data(self):
        """Create required related data if not exists"""
        # Create HR role if not exists
        hr_role, created = Roles.objects.get_or_create(
            rolename='Head of Human Resources',
            defaults={'description': 'Head of Human Resources Department'}
        )

        # Create HR department if not exists
        hr_dept, created = Departments.objects.get_or_create(
            departmentname='Human Resources',
            defaults={'description': 'Human Resources Department'}
        )

        # Create test user for HR HOD
        hr_user, created = Users.objects.get_or_create(
            email='hr.hod@prism.com',
            defaults={
                'username': 'hr_hod',
                'roleid': hr_role,
                'departmentid': hr_dept,
                'phone': '+255 123 456 789',
                'address': 'PRISM HQ, Dar es Salaam',
                'status': 'Active'
            }
        )
        if created:
            hr_user.set_password('testpass123')
            hr_user.save()

        # Create UserProfile for HR HOD
        UserProfile.objects.get_or_create(
            user=hr_user,
            defaults={
                'role': 'hod_human_resources',
                'department': 'Human Resources',
                'phone': '+255 123 456 789'
            }
        )

        # Create other departments for testing
        departments = [
            'Systems Development',
            'Graphics & Animation',
            'Maintenance & Networking',
            'Printing & Publishing',
        ]

        for dept_name in departments:
            Departments.objects.get_or_create(
                departmentname=dept_name,
                defaults={'description': f'{dept_name} Department'}
            )

    def create_employees(self):
        """Create test employees"""
        departments = Departments.objects.all()
        employees_data = [
            {
                'first_name': 'John',
                'last_name': 'Doe',
                'email': 'john.doe@prism.com',
                'phone': '+255 700 123 456',
                'department': 'Systems Development',
                'position': 'Senior Software Developer',
                'salary': 2500000.00,
                'allowance': 150000.00,
                'overtime': 250000.00,
                'hire_date': date(2022, 1, 15),
                'status': 'active',
                'account_number': '1234567890123456'
            },
            {
                'first_name': 'Jane',
                'last_name': 'Smith',
                'email': 'jane.smith@prism.com',
                'phone': '+255 700 234 567',
                'department': 'Graphics & Animation',
                'position': 'Graphic Designer',
                'salary': 1800000.00,
                'allowance': 120000.00,
                'overtime': 180000.00,
                'hire_date': date(2022, 3, 20),
                'status': 'active',
                'account_number': '2345678901234567'
            },
            {
                'first_name': 'Michael',
                'last_name': 'Johnson',
                'email': 'michael.johnson@prism.com',
                'phone': '+255 700 345 678',
                'department': 'Maintenance & Networking',
                'position': 'Network Administrator',
                'salary': 2200000.00,
                'allowance': 140000.00,
                'overtime': 220000.00,
                'hire_date': date(2021, 11, 10),
                'status': 'active',
                'account_number': '3456789012345678'
            },
            {
                'first_name': 'Sarah',
                'last_name': 'Williams',
                'email': 'sarah.williams@prism.com',
                'phone': '+255 700 456 789',
                'department': 'Printing & Publishing',
                'position': 'Print Production Manager',
                'salary': 2000000.00,
                'allowance': 130000.00,
                'overtime': 200000.00,
                'hire_date': date(2022, 5, 5),
                'status': 'active',
                'account_number': '4567890123456789'
            },
            {
                'first_name': 'David',
                'last_name': 'Brown',
                'email': 'david.brown@prism.com',
                'phone': '+255 700 567 890',
                'department': 'Human Resources',
                'position': 'HR Specialist',
                'salary': 1900000.00,
                'allowance': 125000.00,
                'overtime': 190000.00,
                'hire_date': date(2022, 7, 12),
                'status': 'active',
                'account_number': '5678901234567890'
            },
            {
                'first_name': 'Emma',
                'last_name': 'Davis',
                'email': 'emma.davis@prism.com',
                'phone': '+255 700 678 901',
                'department': 'Systems Development',
                'position': 'Junior Developer',
                'salary': 1500000.00,
                'allowance': 100000.00,
                'overtime': 150000.00,
                'hire_date': date(2023, 1, 8),
                'status': 'active',
                'account_number': '6789012345678901'
            },
            {
                'first_name': 'Robert',
                'last_name': 'Miller',
                'email': 'robert.miller@prism.com',
                'phone': '+255 700 789 012',
                'department': 'Graphics & Animation',
                'position': 'Animation Specialist',
                'salary': 2100000.00,
                'allowance': 135000.00,
                'overtime': 210000.00,
                'hire_date': date(2021, 9, 25),
                'status': 'active',
                'account_number': '7890123456789012'
            },
            {
                'first_name': 'Lisa',
                'last_name': 'Wilson',
                'email': 'lisa.wilson@prism.com',
                'phone': '+255 700 890 123',
                'department': 'Maintenance & Networking',
                'position': 'System Administrator',
                'salary': 2300000.00,
                'allowance': 145000.00,
                'overtime': 230000.00,
                'hire_date': date(2022, 2, 18),
                'status': 'active',
                'account_number': '8901234567890123'
            }
        ]

        for emp_data in employees_data:
            dept = Departments.objects.filter(departmentname=emp_data['department']).first()
            if dept:
                Employee.objects.get_or_create(
                    email=emp_data['email'],
                    defaults=emp_data
                )

    def create_payments(self):
        """Create test payments"""
        employees = Employee.objects.all()
        payment_types = ['salary', 'bonus', 'overtime']

        for employee in employees:
            # Create salary payment for current month
            payment_date = timezone.now().replace(day=1)
            Payment.objects.get_or_create(
                employee=employee,
                payment_date=payment_date,
                defaults={
                    'amount': employee.salary,
                    'transaction_id': f'TXN{random.randint(100000, 999999)}',
                    'status': 'success'
                }
            )

            # Create a few more random payments
            for _ in range(random.randint(1, 3)):
                months_ago = random.randint(1, 6)
                payment_date = (timezone.now() - timedelta(days=months_ago * 30)).replace(day=1)
                amount = employee.salary if random.choice([True, False]) else employee.salary * Decimal(str(random.uniform(0.1, 0.5)))

                Payment.objects.get_or_create(
                    employee=employee,
                    payment_date=payment_date,
                    defaults={
                        'amount': amount,
                        'transaction_id': f'TXN{random.randint(100000, 999999)}',
                        'status': random.choice(['success', 'pending', 'failed'])
                    }
                )

    def create_job_requisitions(self):
        """Create test job requisitions"""
        departments = Departments.objects.all()
        hr_user = Users.objects.filter(email='hr.hod@prism.com').first()

        requisitions_data = [
            {
                'position': 'Senior Python Developer',
                'department': 'Systems Development',
                'description': 'We are looking for an experienced Python developer to join our team.',
                'requirements': '5+ years experience, Django expertise, PostgreSQL knowledge',
                'salary_range': '2,500,000 - 3,500,000 TZS',
                'status': 'approved'
            },
            {
                'position': 'UI/UX Designer',
                'department': 'Graphics & Animation',
                'description': 'Creative designer needed for user interface and experience design.',
                'requirements': '3+ years experience, Figma, Adobe Creative Suite',
                'salary_range': '1,800,000 - 2,500,000 TZS',
                'status': 'pending'
            },
            {
                'position': 'Network Security Specialist',
                'department': 'Maintenance & Networking',
                'description': 'Specialist required for network security and monitoring.',
                'requirements': 'CCNA certification, 4+ years experience',
                'salary_range': '2,200,000 - 3,000,000 TZS',
                'status': 'approved'
            },
            {
                'position': 'Print Production Assistant',
                'department': 'Printing & Publishing',
                'description': 'Assistant needed for print production operations.',
                'requirements': '2+ years experience, attention to detail',
                'salary_range': '1,200,000 - 1,800,000 TZS',
                'status': 'pending'
            }
        ]

        for req_data in requisitions_data:
            dept = Departments.objects.filter(departmentname=req_data['department']).first()
            if dept and hr_user:
                JobRequisition.objects.get_or_create(
                    position=req_data['position'],
                    department=dept,
                    defaults={
                        'description': req_data['description'],
                        'requirements': req_data['requirements'],
                        'salary_range': req_data['salary_range'],
                        'requested_by': hr_user,
                        'status': req_data['status']
                    }
                )

    def create_hr_policies(self):
        """Create test HR policies"""
        hr_user = Users.objects.filter(email='hr.hod@prism.com').first()

        policies_data = [
            {
                'title': 'Code of Conduct',
                'content': 'This policy outlines the expected behavior and ethical standards for all employees.',
                'version': '2.1',
                'status': 'active'
            },
            {
                'title': 'Leave Policy',
                'content': 'Guidelines for annual leave, sick leave, and other types of leave.',
                'version': '1.5',
                'status': 'active'
            },
            {
                'title': 'Remote Work Policy',
                'content': 'Policy governing remote work arrangements and requirements.',
                'version': '1.0',
                'status': 'draft'
            },
            {
                'title': 'Data Protection Policy',
                'content': 'Guidelines for handling sensitive data and ensuring compliance with privacy regulations.',
                'version': '1.2',
                'status': 'active'
            }
        ]

        for policy_data in policies_data:
            if hr_user:
                HRPolicy.objects.get_or_create(
                    title=policy_data['title'],
                    defaults={
                        'content': policy_data['content'],
                        'version': policy_data['version'],
                        'status': policy_data['status'],
                        'created_by': hr_user
                    }
                )

    def create_hr_notifications(self):
        """Create test HR notifications"""
        hr_user = Users.objects.filter(email='hr.hod@prism.com').first()

        notifications_data = [
            {
                'title': 'New Policy Update',
                'message': 'The Code of Conduct policy has been updated. Please review the changes.',
                'notification_type': 'policy'
            },
            {
                'title': 'Job Requisition Approved',
                'message': 'Your job requisition for Senior Python Developer has been approved.',
                'notification_type': 'requisition'
            },
            {
                'title': 'Compliance Alert',
                'message': 'Please ensure all employees complete their annual compliance training.',
                'notification_type': 'compliance'
            }
        ]

        for notif_data in notifications_data:
            if hr_user:
                HRNotification.objects.get_or_create(
                    title=notif_data['title'],
                    recipient=hr_user,
                    defaults={
                        'message': notif_data['message'],
                        'notification_type': notif_data['notification_type']
                    }
                )

    def create_financial_reports(self):
        """Create test financial reports"""
        reports_data = [
            'Monthly Financial Report - January 2024',
            'Quarterly Budget Analysis Q1 2024',
            'Annual Financial Summary 2023',
            'Payroll Cost Analysis - December 2023'
        ]

        for report_name in reports_data:
            FinancialReport.objects.get_or_create(
                report_name=report_name
            )

    def create_budget_adjustments(self):
        """Create test budget adjustment requests"""
        hr_user = Users.objects.filter(email='hr.hod@prism.com').first()

        adjustments_data = [
            {
                'category': 'Training & Development',
                'amount': 5000000.00,
                'reason': 'Additional budget needed for employee training programs',
                'status': 'pending'
            },
            {
                'category': 'Recruitment Costs',
                'amount': 3000000.00,
                'reason': 'Increased recruitment needs for new projects',
                'status': 'approved'
            },
            {
                'category': 'Employee Wellness',
                'amount': 2000000.00,
                'reason': 'Budget for wellness programs and activities',
                'status': 'pending'
            }
        ]

        for adj_data in adjustments_data:
            if hr_user:
                BudgetAdjustmentRequest.objects.get_or_create(
                    category=adj_data['category'],
                    amount=adj_data['amount'],
                    defaults={
                        'reason': adj_data['reason'],
                        'requested_by': hr_user,
                        'status': adj_data['status']
                    }
                )

    def create_hr_dashboard(self):
        """Create test HR dashboard data"""
        departments = Departments.objects.all()

        for dept in departments:
            HRDashboard.objects.get_or_create(
                department=dept,
                defaults={
                    'total_headcount': random.randint(5, 25),
                    'open_requisitions': random.randint(0, 5),
                    'high_priority_cases': random.randint(0, 3),
                    'compliance_alerts': random.randint(0, 2),
                    'turnover_rate': round(random.uniform(2.0, 8.0), 2),
                    'avg_hire_time': random.randint(30, 60),
                    'satisfaction_score': round(random.uniform(7.0, 9.5), 1),
                    'budget_utilization': round(random.uniform(50.0, 85.0), 2)
                }
            )
