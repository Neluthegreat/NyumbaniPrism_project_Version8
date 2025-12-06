from django.test import TestCase
from .models import Employee

class EmployeeTestCase(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create(
            first_name="Jane",
            last_name="Doe",
            email="jane.doe@company.com",
            phone="1234567890",
            department="Marketing",
            position="Manager",
            salary=75000.00,
            hire_date="2023-01-15",
            status="active"
        )
    
    def test_employee_creation(self):
        self.assertEqual(str(self.employee), "Jane Doe")
        self.assertEqual(self.employee.full_name, "Jane Doe")
        self.assertEqual(self.employee.status, "active")
