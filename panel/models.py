from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone

class Addresses(models.Model):
    addressid = models.AutoField(primary_key=True)
    entitytype = models.CharField(max_length=50, blank=True, null=True)
    entityid = models.IntegerField(blank=True, null=True)
    addresstype = models.CharField(max_length=50, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    zip = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    updatedat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'addresses'

class Appointments(models.Model):
    appointmentid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    starttime = models.DateTimeField(blank=True, null=True)
    endtime = models.DateTimeField(blank=True, null=True)
    projectid = models.ForeignKey('Projects', models.DO_NOTHING, db_column='projectid', blank=True, null=True)
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid', blank=True, null=True)
    customerid = models.ForeignKey('Customers', models.DO_NOTHING, db_column='customerid', blank=True, null=True)
    location_url = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    updatedat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'appointments'

class Attendance(models.Model):
    attendanceid = models.AutoField(primary_key=True)
    employeeid = models.ForeignKey('Employees', models.DO_NOTHING, db_column='employeeid', blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    checkintime = models.TimeField(blank=True, null=True)
    checkouttime = models.TimeField(blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    updatedat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attendance'

class AuditLog(models.Model):
    logid = models.AutoField(primary_key=True)
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid', blank=True, null=True)
    action = models.CharField(max_length=255, blank=True, null=True)
    tablename = models.CharField(max_length=255, blank=True, null=True)
    recordid = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'audit_log'

class Bills(models.Model):
    billid = models.AutoField(primary_key=True)
    departmentid = models.ForeignKey('Departments', models.DO_NOTHING, db_column='departmentid', blank=True, null=True)
    employeeid = models.ForeignKey('Employees', models.DO_NOTHING, db_column='employeeid', blank=True, null=True)
    inventoryid = models.ForeignKey('Inventory', models.DO_NOTHING, db_column='inventoryid', blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    billtype = models.CharField(max_length=255, blank=True, null=True)
    billdate = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    updatedat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bills'

class Budgets(models.Model):
    budgetid = models.AutoField(primary_key=True)
    departmentid = models.ForeignKey('Departments', models.DO_NOTHING, db_column='departmentid', blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    updatedat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'budgets'

class ChartOfAccounts(models.Model):
    accountid = models.AutoField(primary_key=True)
    accountname = models.CharField(max_length=255, blank=True, null=True)
    accounttype = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    departmentid = models.ForeignKey('Departments', models.DO_NOTHING, db_column='departmentid', blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    updatedat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chart_of_accounts'

class ChecklistItems(models.Model):
    checklistitemid = models.AutoField(primary_key=True)
    checklistid = models.ForeignKey('Checklists', models.DO_NOTHING, db_column='checklistid', blank=True, null=True)
    itemtext = models.TextField(blank=True, null=True)
    itemorder = models.IntegerField(blank=True, null=True)
    itemtype = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'checklist_items'

class Checklists(models.Model):
    checklistid = models.AutoField(primary_key=True)
    checklistname = models.CharField(max_length=255, blank=True, null=True)
    departmentid = models.ForeignKey('Departments', models.DO_NOTHING, db_column='departmentid', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'checklists'

class ComplianceRecords(models.Model):
    compliancerecordid = models.AutoField(primary_key=True)
    employeeid = models.ForeignKey('Employees', models.DO_NOTHING, db_column='employeeid', blank=True, null=True)
    certificatename = models.CharField(max_length=255, blank=True, null=True)
    issuingbody = models.CharField(max_length=255, blank=True, null=True)
    issuedate = models.DateField(blank=True, null=True)
    expirydate = models.DateField(blank=True, null=True)
    documentpath = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compliance_records'

class CustomerCommunications(models.Model):
    communicationid = models.AutoField(primary_key=True)
    customerid = models.ForeignKey('Customers', models.DO_NOTHING, db_column='customerid', blank=True, null=True)
    leadid = models.ForeignKey('Leads', models.DO_NOTHING, db_column='leadid', blank=True, null=True)
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid', blank=True, null=True)
    communicationtype = models.CharField(max_length=50, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    communicationtimestamp = models.DateTimeField(blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_communications'

class Customers(models.Model):
    customerid = models.AutoField(primary_key=True)
    customername = models.CharField(max_length=255, null=False)
    contactperson = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=False)
    phone = models.CharField(max_length=50, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, default='Active')

    def __str__(self):
        return self.customername

    class Meta:
        managed = False
        db_table = 'customers'

class Departments(models.Model):
    departmentid = models.AutoField(primary_key=True)
    departmentname = models.CharField(max_length=255, null=False)
    description = models.TextField()
    hodid = models.ForeignKey('Users', on_delete=models.SET_NULL, null=True, blank=True, db_column='hodid')  # Updated line

    def __str__(self):
        return self.departmentname

    class Meta:
        managed = False
        db_table = 'departments'

class Documents(models.Model):
    documentid = models.AutoField(primary_key=True)
    projectid = models.ForeignKey('Projects', models.DO_NOTHING, db_column='projectid', blank=True, null=True)
    customerid = models.ForeignKey('Customers', models.DO_NOTHING, db_column='customerid', blank=True, null=True)
    filepath = models.CharField(max_length=255, blank=True, null=True)
    filename = models.CharField(max_length=255, blank=True, null=True)
    version = models.CharField(max_length=50, blank=True, null=True)
    documenttype = models.CharField(max_length=255, blank=True, null=True)
    createdby = models.ForeignKey('Users', models.DO_NOTHING, db_column='createdby', blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    updatedat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documents'

class EmployeeSkills(models.Model):
    employeeskillid = models.AutoField(primary_key=True)
    employeeid = models.ForeignKey('Employees', models.DO_NOTHING, db_column='employeeid', blank=True, null=True)
    skillid = models.ForeignKey('Skills', models.DO_NOTHING, db_column='skillid', blank=True, null=True)
    proficiencylevel = models.CharField(max_length=50, blank=True, null=True)
    lastverifieddate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee_skills'

class Employees(models.Model):
    employeeid = models.AutoField(primary_key=True)
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid')
    departmentid = models.ForeignKey('Departments', models.DO_NOTHING, db_column='departmentid')
    position = models.CharField(max_length=255, blank=True, null=True)
    hiredate = models.DateField(blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    updatedat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employees'

class FinancialTransactions(models.Model):
    transactionid = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    projectid = models.ForeignKey('Projects', models.DO_NOTHING, db_column='projectid', blank=True, null=True)
    departmentid = models.ForeignKey('Departments', models.DO_NOTHING, db_column='departmentid', blank=True, null=True)
    categoryid = models.ForeignKey('TransactionCategories', models.DO_NOTHING, db_column='categoryid', blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    updatedat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'financial_transactions'

class HrCases(models.Model):
    caseid = models.AutoField(primary_key=True)
    employeeid = models.ForeignKey('Employees', models.DO_NOTHING, db_column='employeeid', blank=True, null=True)
    casemanageruserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='casemanageruserid', blank=True, null=True)
    casetype = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    dateopened = models.DateField(blank=True, null=True)
    dateclosed = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_cases'

class Inventory(models.Model):
    inventoryid = models.AutoField(primary_key=True)
    itemname = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    unitprice = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    totalvalue = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    departmentid = models.ForeignKey('Departments', models.DO_NOTHING, db_column='departmentid', blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    updatedat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventory'

class InventoryMovements(models.Model):
    movementid = models.AutoField(primary_key=True)
    inventoryid = models.ForeignKey('Inventory', models.DO_NOTHING, db_column='inventoryid', blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid', blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    updatedat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventory_movements'

class KnowledgebaseArticles(models.Model):
    articleid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid', blank=True, null=True)
    ispublic = models.BooleanField(blank=True, null=True)
    categoryid = models.IntegerField(blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    updatedat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'knowledgebase_articles'

class Leads(models.Model):
    leadid = models.AutoField(primary_key=True)
    customerid = models.ForeignKey('Customers', models.DO_NOTHING, db_column='customerid', blank=True, null=True)
    campaignid = models.ForeignKey('MarketingCampaigns', models.DO_NOTHING, db_column='campaignid', blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    updatedat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'leads'

class LeaveRequests(models.Model):
    leaveid = models.AutoField(primary_key=True)
    employeeid = models.ForeignKey('Employees', models.DO_NOTHING, db_column='employeeid', blank=True, null=True)
    startdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    updatedat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'leave_requests'

class MarketingCampaigns(models.Model):
    campaignid = models.AutoField(primary_key=True)
    campaignname = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    startdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    updatedat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marketing_campaigns'

class OrderItems(models.Model):
    orderitemid = models.AutoField(primary_key=True)
    orderid = models.ForeignKey('Orders', models.DO_NOTHING, db_column='orderid', blank=True, null=True)
    inventoryid = models.ForeignKey('Inventory', models.DO_NOTHING, db_column='inventoryid', blank=True, null=True)
    productid = models.ForeignKey('ProductsServices', models.DO_NOTHING, db_column='productid', blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    unitprice = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    totalprice = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    updatedat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_items'

class Orders(models.Model):
    orderid = models.AutoField(primary_key=True)
    customerid = models.ForeignKey('Customers', models.DO_NOTHING, db_column='customerid', blank=True, null=True)
    quoteid = models.ForeignKey('Quotes', models.DO_NOTHING, db_column='quoteid', blank=True, null=True)
    orderdate = models.DateField(blank=True, null=True)
    totalamount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    updatedat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'

class Payments(models.Model):
    paymentid = models.AutoField(primary_key=True)
    orderid = models.ForeignKey('Orders', models.DO_NOTHING, db_column='orderid', blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    paymentmethod = models.CharField(max_length=50, blank=True, null=True)
    paymentdate = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    updatedat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payments'

class PayrollDeductions(models.Model):
    deductionid = models.AutoField(primary_key=True)
    employeeid = models.ForeignKey('Employees', models.DO_NOTHING, db_column='employeeid', blank=True, null=True)
    transactionid = models.ForeignKey('FinancialTransactions', models.DO_NOTHING, db_column='transactionid', blank=True, null=True)
    deductiontype = models.CharField(max_length=255, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    dateofdeduction = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid', blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payroll_deductions'

class Permissions(models.Model):
    permissionid = models.AutoField(primary_key=True)
    roleid = models.ForeignKey('Roles', models.DO_NOTHING, db_column='roleid', blank=True, null=True)
    module = models.CharField(max_length=255, blank=True, null=True)
    accesslevel = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permissions'

class ProductsServices(models.Model):
    productid = models.AutoField(primary_key=True)
    departmentid = models.ForeignKey('Departments', models.DO_NOTHING, db_column='departmentid', blank=True, null=True)
    productname = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    unitprice = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    updatedat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products_services'

class ProfitCalculations(models.Model):
    profitid = models.AutoField(primary_key=True)
    period = models.CharField(max_length=50, blank=True, null=True)
    totalincome = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    totalexpenses = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    netprofit = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    departmentid = models.ForeignKey('Departments', models.DO_NOTHING, db_column='departmentid', blank=True, null=True)
    projectid = models.ForeignKey('Projects', models.DO_NOTHING, db_column='projectid', blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    updatedat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profit_calculations'

class Projects(models.Model):
    projectid = models.AutoField(primary_key=True)
    projectname = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    departmentid = models.ForeignKey('Departments', models.DO_NOTHING, db_column='departmentid', blank=True, null=True)
    customerid = models.ForeignKey('Customers', models.DO_NOTHING, db_column='customerid', blank=True, null=True)
    startdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    updatedat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'projects'

class PurchaseOrderItems(models.Model):
    poitemid = models.AutoField(primary_key=True)
    purchaseorderid = models.ForeignKey('PurchaseOrders', models.DO_NOTHING, db_column='purchaseorderid', blank=True, null=True)
    productid = models.ForeignKey('ProductsServices', models.DO_NOTHING, db_column='productid', blank=True, null=True)
    inventoryid = models.ForeignKey('Inventory', models.DO_NOTHING, db_column='inventoryid', blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    unitprice = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    totalprice = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'purchase_order_items'

class PurchaseOrders(models.Model):
    purchaseorderid = models.AutoField(primary_key=True)
    vendorid = models.ForeignKey('Vendors', models.DO_NOTHING, db_column='vendorid', blank=True, null=True)
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid', blank=True, null=True)
    orderdate = models.DateField(blank=True, null=True)
    totalamount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    requisitionid = models.ForeignKey('Requisitions', models.DO_NOTHING, db_column='requisitionid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'purchase_orders'

class QuoteItems(models.Model):
    quoteitemid = models.AutoField(primary_key=True)
    quoteid = models.ForeignKey('Quotes', models.DO_NOTHING, db_column='quoteid', blank=True, null=True)
    inventoryid = models.ForeignKey('Inventory', models.DO_NOTHING, db_column='inventoryid', blank=True, null=True)
    productid = models.ForeignKey('ProductsServices', models.DO_NOTHING, db_column='productid', blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    unitprice = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    totalprice = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    updatedat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quote_items'

class Quotes(models.Model):
    quoteid = models.AutoField(primary_key=True)
    customerid = models.ForeignKey('Customers', models.DO_NOTHING, db_column='customerid', blank=True, null=True)
    departmentid = models.ForeignKey('Departments', models.DO_NOTHING, db_column='departmentid', blank=True, null=True)
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid', blank=True, null=True)
    quotedate = models.DateField(blank=True, null=True)
    totalamount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    updatedat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quotes'

class RequisitionItems(models.Model):
    requisitionitemid = models.AutoField(primary_key=True)
    requisitionid = models.ForeignKey('Requisitions', models.DO_NOTHING, db_column='requisitionid', blank=True, null=True)
    productname = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    estimatedprice = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'requisition_items'

class Requisitions(models.Model):
    requisitionid = models.AutoField(primary_key=True)
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid', blank=True, null=True)
    departmentid = models.ForeignKey('Departments', models.DO_NOTHING, db_column='departmentid', blank=True, null=True)
    requestdate = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    justification = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'requisitions'

class ResourceBookings(models.Model):
    bookingid = models.AutoField(primary_key=True)
    assetid = models.ForeignKey('Inventory', models.DO_NOTHING, db_column='assetid', blank=True, null=True)
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid', blank=True, null=True)
    projectid = models.ForeignKey('Projects', models.DO_NOTHING, db_column='projectid', blank=True, null=True)
    starttime = models.DateTimeField(blank=True, null=True)
    endtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resource_bookings'

class Roles(models.Model):
    roleid = models.AutoField(primary_key=True)
    rolename = models.CharField(max_length=255, null=False)
    description = models.TextField()

    def __str__(self):
        return self.rolename

    class Meta:
        managed = False
        db_table = 'roles'

class ServiceTickets(models.Model):
    ticketid = models.AutoField(primary_key=True)
    customerid = models.ForeignKey('Customers', models.DO_NOTHING, db_column='customerid', blank=True, null=True)
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid', blank=True, null=True)
    assetid = models.ForeignKey('Inventory', models.DO_NOTHING, db_column='assetid', blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    priority = models.CharField(max_length=50, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    resolutiondetails = models.TextField(blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    updatedat = models.DateTimeField(blank=True, null=True)
    closedat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service_tickets'

class Skills(models.Model):
    skillid = models.AutoField(primary_key=True)
    skillname = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'skills'

class SurveyQuestions(models.Model):
    questionid = models.AutoField(primary_key=True)
    surveyid = models.IntegerField(blank=True, null=True)
    questiontext = models.TextField(blank=True, null=True)
    questiontype = models.CharField(max_length=50, blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey_questions'

class SurveyResponses(models.Model):
    responseid = models.AutoField(primary_key=True)
    questionid = models.ForeignKey('SurveyQuestions', models.DO_NOTHING, db_column='questionid', blank=True, null=True)
    customerid = models.ForeignKey('Customers', models.DO_NOTHING, db_column='customerid', blank=True, null=True)
    responsevalue = models.TextField(blank=True, null=True)
    submittedat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey_responses'

class TaskChecklistResults(models.Model):
    resultid = models.AutoField(primary_key=True)
    taskid = models.ForeignKey('Tasks', models.DO_NOTHING, db_column='taskid', blank=True, null=True)
    checklistitemid = models.ForeignKey('ChecklistItems', models.DO_NOTHING, db_column='checklistitemid', blank=True, null=True)
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid', blank=True, null=True)
    result = models.CharField(max_length=50, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'task_checklist_results'

class Tasks(models.Model):
    taskid = models.AutoField(primary_key=True)
    projectid = models.ForeignKey('Projects', models.DO_NOTHING, db_column='projectid', blank=True, null=True)
    taskname = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    assignedto = models.ForeignKey('Users', models.DO_NOTHING, db_column='assignedto', blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    duedate = models.DateField(blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    updatedat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tasks'

class TimeTracking(models.Model):
    timetrackingid = models.AutoField(primary_key=True)
    taskid = models.ForeignKey('Tasks', models.DO_NOTHING, db_column='taskid', blank=True, null=True)
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid', blank=True, null=True)
    starttime = models.DateTimeField(blank=True, null=True)
    endtime = models.DateTimeField(blank=True, null=True)
    duration = models.DurationField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'time_tracking'

class TransactionCategories(models.Model):
    categoryid = models.AutoField(primary_key=True)
    categoryname = models.CharField(max_length=255)
    type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transaction_categories'

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        if not username:
            raise ValueError('The Username field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('status', 'Active')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, username, password, **extra_fields)

class Users(AbstractBaseUser, PermissionsMixin):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True, null=False)
    email = models.EmailField(unique=True, null=False)
    roleid = models.ForeignKey('Roles', on_delete=models.CASCADE, null=True, db_column='roleid')
    departmentid = models.ForeignKey('Departments', on_delete=models.SET_NULL, null=True, blank=True, db_column='departmentid')
    phone = models.CharField(max_length=50, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, default='Active')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = 'users'
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['username']),
        ]

class Vendors(models.Model):
    vendorid = models.AutoField(primary_key=True)
    vendorname = models.CharField(max_length=255, blank=True, null=True)
    contactperson = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    updatedat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vendors'

# Duplicate and mis-indented Requisitions class removed to fix indentation and class redefinition errors.