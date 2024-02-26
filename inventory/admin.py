from django.contrib import admin
from inventory.models import Account
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import *

class AccountInLine(admin.StackedInline):
    model = Account
    can_delete = False

class CustomizedUserAdmin (UserAdmin):
    inlines = (AccountInLine, )
admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)
    ordering = ('name',)
    search_fields = ('name',)

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    fields = ('user', 'branch')
    list_display = ('user', 'branch')
    ordering = ('user', 'branch')
    search_fields = ('user', 'branch')

@admin.register(CoMaker)
class CoMakerAdmin(admin.ModelAdmin):
    fields = ('last_name', 'first_name', 'middle_name', 'address')
    list_display = ('last_name', 'first_name', 'middle_name', 'address')
    ordering = ('last_name',)
    search_fields = ('last_name', 'first_name', 'middle_name')

@admin.register(Payment)
class Payment(admin.ModelAdmin):
    fields = ('date_release', 'loan_type', 'selling_price', 'down_payment', 'amount_finance', 'terms_of_payment',
               'monthly_installment', 'promisory_note', 'discount', 'registration_number', 'OR_number', 'remarks',
               'residence_number', 'DPS', 'ROPOA')
    list_display = ('date_release', 'loan_type', 'selling_price', 'down_payment', 'amount_finance', 'terms_of_payment',
               'monthly_installment', 'promisory_note', 'discount', 'registration_number', 'OR_number', 'remarks',
               'residence_number', 'DPS', 'ROPOA')
    ordering = ('OR_number',)
    search_fields = ('OR_number',)

@admin.register(Supplier)
class Supplier(admin.ModelAdmin):
    fields = ('name', 'address')
    list_display = ('name', 'address')
    ordering = ('name',)
    search_fields = ('name', 'address')

@admin.register(BranchType)
class BranchType(admin.ModelAdmin):
    list_display = ('branch_type',)
    ordering = ('branch_type',)
    search_fields = ('branch_type',)

@admin.register(Branch)
class Branch(admin.ModelAdmin):
    fields = ('id', 'code', 'name', 'address', 'phone_number', 'branchtype')
    list_display = ('id', 'code', 'name', 'address', 'phone_number', 'branchtype')
    ordering = ('code',)
    search_fields = ('code', 'name')

@admin.register(Receive)
class Receive(admin.ModelAdmin):
    fields = (('RR_number','PO_number', 'STS_number'), 'supplier', 'branch', 'delivery_date', 'terms')
    list_display = ('RR_number','PO_number', 'supplier', 'STS_number', 'delivery_date', 'terms')
    ordering = ('RR_number',)
    search_fields = ('RR_number','PO_number')

@admin.register(Motor)
class Motor(admin.ModelAdmin):
    fields = ('brand', 'model', 'frame_start', 'engine_start')
    list_display = ('brand', 'model', 'frame_start', 'engine_start')
    ordering = ('brand', 'model',)
    search_fields = ('brand__brand_name', 'model')

@admin.register(MotorColor)
class MotorColor(admin.ModelAdmin):
    fields = ('code', 'name')
    list_display = ('code', 'name')
    ordering = ('code', 'name',)
    search_fields = ('code', 'name')

@admin.register(Inventory)
class Inventory(admin.ModelAdmin):
    fields = ('receive','motor', 'motor_color', 'frame_number', 'engine_number')
    list_display = ('motor', 'motor_color', 'frame_number', 'engine_number',)
    ordering = ('engine_number',)
    search_fields = ('engine_number',)

@admin.register(SalesType)
class SalesType(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
    search_fields = ('name',)

@admin.register(Customer)
class Customer(admin.ModelAdmin):
    fields = ('last_name', 'first_name', 'middle_name', 'address', 'status', 
                    'phone_number', 'residence_number','comaker')
    list_display = ('last_name', 'first_name', 'middle_name', 'address', 'status', 
                    'phone_number', 'residence_number')
    ordering = ('last_name',)
    search_fields = ('last_name', 'first_name', 'middle_name')

@admin.register(Customer_Released)
class Customer_Released(admin.ModelAdmin):
    fields = ('branch', 'customer', 'comaker', 'salestype', 'payment', 'inventory')
    list_display = ('branch', 'customer', 'comaker', 'salestype', 'payment', 'inventory')
    ordering = ('id','branch', 'customer', 'comaker', 'salestype', 'payment', 'inventory')
    search_fields = ('branch', 'customer','comaker','salestype','payment','inventory')

@admin.register(Transfer)
class Transfer(admin.ModelAdmin):
    fields = ('status', 'transferfrom', 'transferto', 'controlnumber', 'transferout_date', 'transferin_date', 'inventory')
    list_display = ('status', 'transferfrom', 'transferto', 'controlnumber', 'transferout_date', 'transferin_date', 'inventory')
    ordering = ('controlnumber',)
    search_fields = ('controlnumber',)

@admin.register(RepoIn)
class RepoIn(admin.ModelAdmin):
    fields = ('branch','inventory')
    list_display = ('branch','inventory')
    ordering = ('branch','inventory')
    search_fields = ('branch','inventory')

@admin.register(RepoOut)
class RepoOut(admin.ModelAdmin):
    fields = ('branch', 'customer','comaker','salestype','payment','inventory')
    list_display = ('branch', 'customer','comaker','salestype','payment','inventory')
    ordering = ('id', 'branch', 'customer','comaker','salestype','payment','inventory')
    search_fields = ('branch', 'customer','comaker','salestype','payment','inventory')
