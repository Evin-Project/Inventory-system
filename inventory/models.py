from django.db import models
from django.contrib.auth.models import User

class BranchType(models.Model):
    branch_type = models.CharField('Branch Type', max_length=60, null=True)

    def __str__(self):
        return self.branch_type

class Branch(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    code = models.CharField('Branch Code', max_length=60, null=True, blank=True)
    name = models.CharField('Branch Name', max_length=60, null=True, blank=True)
    address = models.CharField('Branch Address', max_length=100, null=True, blank=True)
    phone_number = models.CharField('Phone Number', max_length=15, null=True, blank=True)
    branchtype = models.ForeignKey(BranchType, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.code

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user) + ' ' + self.branch.code

class Supplier(models.Model):
    name = models.CharField('Supplier Name', max_length=100, null=True, blank=True)
    address = models.CharField('Supplier Address', max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class MotorColor(models.Model):
    code = models.CharField('Motor Color Code', max_length=60, null=True, blank=True)
    name = models.CharField('Motor Color Name', max_length=60, null=True, blank=True)

    def __str__(self):
        return self.code + ' - ' + self.name

class Motor(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    brand = models.ForeignKey(Supplier, max_length=60, null=True, blank=True, on_delete=models.CASCADE)
    model = models.CharField('Model', max_length=60, null=True, blank=True)
    frame_start = models.CharField('Frame Start', max_length=60, null=True, blank=True)
    engine_start = models.CharField('Engine Start', max_length=60, null=True, blank=True)

    def __str__(self):
        return self.model

class Status(models.Model):
    name = models.CharField('Status', max_length=60, null=True, blank=True)

    def __str__(self):
        return self.name

class Receive(models.Model):
    RR_number = models.IntegerField('RR Number', null=True, blank=True)
    PO_number = models.IntegerField('PO Number', null=True, blank=True)
    supplier = models.ForeignKey(Supplier, blank=True, null=True, on_delete=models.CASCADE)
    STS_number = models.IntegerField('STS Number', null=True, blank=True)
    delivery_date = models.DateField('Delivery Date', null=True, blank=True)
    terms = models.IntegerField('Terms', null=True, blank=True)
    branch = models.ForeignKey(Branch, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.RR_number)

class Inventory(models.Model):
    status = models.ForeignKey(Status, blank=True, null=True, on_delete=models.CASCADE)
    receive = models.ForeignKey(Receive, blank=True, null=True, on_delete=models.CASCADE)
    motor = models.ForeignKey(Motor, blank=True, null=True, on_delete=models.CASCADE)
    motor_color = models.ForeignKey(MotorColor, blank=True, null=True, on_delete=models.CASCADE)
    frame_number = models.CharField('Frame Number', max_length=60, null=True, blank=True)
    engine_number = models.CharField('Engine Number', max_length=60, null=True, blank=True)
    branch = models.ForeignKey(Branch, blank=True, null=True, on_delete=models.CASCADE)
    

    def __str__(self):
        return str(self.receive.RR_number) + ' - ' + (self.motor.model)

class Transfer(models.Model):
    status = models.ForeignKey(Status, blank=True, null=True, on_delete=models.CASCADE)
    transferfrom = models.ForeignKey(Branch, blank=True, null=True, on_delete=models.CASCADE, related_name='transfers_from_branch')
    transferto = models.ForeignKey(Branch, blank=True, null=True, on_delete=models.CASCADE, related_name='transfers_to_branch')
    controlnumber = models.IntegerField('Control Number', null=True, blank=True)
    transferout_date = models.DateField('Transfer Out Date', null=True, blank=True)
    transferin_date = models.DateField('Transfer In Date', null=True, blank=True)
    inventory = models.ForeignKey(Inventory, blank=True, null=True, on_delete=models.CASCADE, related_name='transfers')

    def __str__(self):
        return str(self.controlnumber)

class Customer(models.Model):
    last_name = models.CharField('Last Name', max_length=60, null=True, blank=True)
    first_name = models.CharField('First Name', max_length=60, null=True, blank=True)
    middle_name = models.CharField('Middle Name', max_length=60, null=True, blank=True)
    address = models.CharField('Address', max_length=100, null=True, blank=True)
    status = models.CharField('Status', max_length=60, null=True, blank=True)
    phone_number = models.CharField('Phone Number', max_length=15, null=True, blank=True)
    residence_number = models.CharField('Residence Number', max_length=60, null=True, blank=True)
    branch = models.ForeignKey(Branch, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        fields = [field for field in [self.last_name, self.first_name, self.middle_name] if field is not None]
        return ' '.join(fields)

class CoMaker(models.Model):
    last_name = models.CharField('Last Name', max_length=60, null=True)
    first_name = models.CharField('First Name', max_length=60, null=True)
    middle_name = models.CharField('Middle Name', max_length=60, null=True, blank=True)
    address = models.CharField('Address', max_length=100, null=True, blank=True)
    branch = models.ForeignKey(Branch, blank=True, null=True, on_delete=models.CASCADE)


    def __str__(self):
        fields = [field for field in [self.last_name, self.first_name, self.middle_name] if field is not None]
        return ' '.join(fields)

class Payment(models.Model):
    date_release = models.DateField('Date Release', null=True, blank=True)
    loan_type = models.CharField('Loan Type', max_length=100, null=True, blank=True)
    selling_price = models.DecimalField('Selling Price', max_digits=20, decimal_places=2, null=True, blank=True)
    down_payment = models.DecimalField('Down Payment', max_digits=20, decimal_places=2, null=True, blank=True)
    amount_finance = models.DecimalField('Amount Finance', max_digits=20, decimal_places=2, null=True, blank=True)
    terms_of_payment = models.CharField('Terms of Payment', max_length=60, null=True, blank=True)
    monthly_installment = models.DecimalField('Monthly Installment', max_digits=20, decimal_places=2, null=True, blank=True)
    promisory_note = models.DecimalField('Promisory Note', max_digits=20, decimal_places=2, null=True, blank=True)
    discount = models.DecimalField('Discount', max_digits=20, decimal_places=2, null=True, blank=True)
    registration_number = models.CharField('Registration Number', max_length=60, null=True, blank=True)
    OR_number = models.CharField('OR Number', max_length=60, null=True, blank=True)
    remarks = models.CharField('Remarks', max_length=60, null=True, blank=True)
    residence_number = models.CharField('Residence Number', max_length=60, null=True, blank=True)
    DPS = models.DecimalField('DPS', max_digits=20, decimal_places=2, null=True, blank=True)
    ROPOA = models.DecimalField('ROPOA', max_digits=20, decimal_places=2, null=True, blank=True)
    branch = models.ForeignKey(Branch, blank=True, null=True, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.OR_number) if self.OR_number is not None else 'No OR Number'

class SalesType(models.Model):
    name = models.CharField('Sales Type', max_length=60, null=True, blank=True)

    def __str__(self):
        return self.name

class Customer_Released(models.Model):
    customer = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.CASCADE)
    comaker = models.ForeignKey(CoMaker, blank=True, null=True, on_delete=models.CASCADE)
    salestype = models.ForeignKey(SalesType, null=True, blank=True, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, blank=True, null=True, on_delete=models.CASCADE)
    inventory = models.ForeignKey(Inventory, blank=True, null=True, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, blank=True, null=True, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.id)

class RepoIn(models.Model):
    inventory = models.ForeignKey(Inventory, blank=True, null=True, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, blank=True, null=True, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.inventory)

class RepoOut(models.Model):
    customer = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.CASCADE)
    comaker = models.ForeignKey(CoMaker, blank=True, null=True, on_delete=models.CASCADE)
    salestype = models.ForeignKey(SalesType, null=True, blank=True, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, blank=True, null=True, on_delete=models.CASCADE)
    inventory = models.ForeignKey(Inventory, blank=True, null=True, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, blank=True, null=True, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.id)
