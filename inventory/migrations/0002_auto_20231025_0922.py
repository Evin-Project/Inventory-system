# Generated by Django 3.0.7 on 2023-10-25 01:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=60, null=True, verbose_name='Branch Code')),
                ('name', models.CharField(blank=True, max_length=60, null=True, verbose_name='Branch Name')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Branch Address')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True, verbose_name='Phone Number')),
            ],
        ),
        migrations.CreateModel(
            name='BranchType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_type', models.CharField(max_length=60, null=True, verbose_name='Branch Type')),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=60, null=True, verbose_name='Brand')),
            ],
        ),
        migrations.CreateModel(
            name='CoMaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=60, null=True, verbose_name='Last Name')),
                ('first_name', models.CharField(max_length=60, null=True, verbose_name='First Name')),
                ('middle_name', models.CharField(blank=True, max_length=60, null=True, verbose_name='Middle Name')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Address')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(blank=True, max_length=60, null=True, verbose_name='Last Name')),
                ('first_name', models.CharField(blank=True, max_length=60, null=True, verbose_name='First Name')),
                ('middle_name', models.CharField(blank=True, max_length=60, null=True, verbose_name='Middle Name')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Address')),
                ('status', models.CharField(blank=True, max_length=60, null=True, verbose_name='Status')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True, verbose_name='Phone Number')),
                ('residence_number', models.CharField(blank=True, max_length=60, null=True, verbose_name='Residence Number')),
                ('comaker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.CoMaker')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frame_number', models.CharField(blank=True, max_length=60, null=True, verbose_name='Frame Number')),
                ('engine_number', models.CharField(blank=True, max_length=60, null=True, verbose_name='Engine Number')),
            ],
        ),
        migrations.CreateModel(
            name='Motor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(blank=True, max_length=60, null=True, verbose_name='Model')),
                ('frame_start', models.CharField(blank=True, max_length=60, null=True, verbose_name='Frame Start')),
                ('engine_start', models.CharField(blank=True, max_length=60, null=True, verbose_name='Engine Start')),
                ('brand', models.ForeignKey(blank=True, max_length=60, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.Brand')),
            ],
        ),
        migrations.CreateModel(
            name='MotorColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=60, null=True, verbose_name='Motor Color Code')),
                ('name', models.CharField(blank=True, max_length=60, null=True, verbose_name='Motor Color Name')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_release', models.DateField(null=True, verbose_name='Date Release')),
                ('loan_type', models.CharField(blank=True, max_length=100, null=True, verbose_name='Loan Type')),
                ('selling_price', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Selling Price')),
                ('down_payment', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Down Payment')),
                ('amount_finance', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Amount Finance')),
                ('terms_of_payment', models.CharField(blank=True, max_length=60, null=True, verbose_name='Terms of Payment')),
                ('monthly_installment', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Monthly Installment')),
                ('promisory_note', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Promisory Note')),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Discount')),
                ('registration_number', models.CharField(blank=True, max_length=60, null=True, verbose_name='Registration Number')),
                ('OR_number', models.CharField(blank=True, max_length=60, null=True, verbose_name='OR Number')),
                ('remarks', models.CharField(blank=True, max_length=60, null=True, verbose_name='Remarks')),
                ('residence_number', models.CharField(blank=True, max_length=60, null=True, verbose_name='Residence Number')),
                ('DPS', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='DPS')),
                ('ROPOA', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='ROPOA')),
            ],
        ),
        migrations.CreateModel(
            name='SalesType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=60, null=True, verbose_name='Sales Type')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Supplier Name')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Supplier Address')),
            ],
        ),
        migrations.CreateModel(
            name='TransactionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=60, null=True, verbose_name='Transaction Name')),
            ],
        ),
        migrations.CreateModel(
            name='TransferOut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('controlnumber', models.IntegerField(blank=True, null=True, verbose_name='ControlNumber')),
                ('date', models.DateField(null=True, verbose_name='Date Release')),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.Branch')),
                ('motor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.Motor')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('control_number', models.IntegerField(blank=True, null=True, verbose_name='Control Number')),
                ('transaction_date', models.DateTimeField(blank=True, null=True, verbose_name='Transaction Date')),
                ('account', models.ManyToManyField(blank=True, to='inventory.Account')),
                ('inventory', models.ManyToManyField(blank=True, to='inventory.Inventory')),
                ('transaction_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.TransactionType')),
            ],
        ),
        migrations.CreateModel(
            name='Receive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RR_number', models.IntegerField(blank=True, null=True, verbose_name='RR Number')),
                ('PO_number', models.IntegerField(blank=True, null=True, verbose_name='PO Number')),
                ('STS_number', models.IntegerField(blank=True, null=True, verbose_name='STS Number')),
                ('delivery_date', models.DateField(blank=True, null=True, verbose_name='Delivery Date')),
                ('terms', models.IntegerField(blank=True, null=True, verbose_name='Terms')),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.Branch')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.Supplier')),
            ],
        ),
        migrations.AddField(
            model_name='inventory',
            name='motor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.Motor'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='motor_color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.MotorColor'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='receive',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.Receive'),
        ),
        migrations.CreateModel(
            name='Customer_History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.Customer')),
                ('inventory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.Inventory')),
                ('payment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.Payment')),
                ('salestype', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.SalesType')),
            ],
        ),
        migrations.AddField(
            model_name='branch',
            name='branchtype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.BranchType'),
        ),
        migrations.AddField(
            model_name='account',
            name='branch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.Branch'),
        ),
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]