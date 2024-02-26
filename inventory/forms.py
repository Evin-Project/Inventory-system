from django import forms
from .models import *
from django.contrib.auth.models import User
from django.forms import inlineformset_factory
    
  


# this form use to addsupplier html
class SupplierForm(forms.ModelForm):
    class Meta:
        # Define the metadata for the form, specifying the model and fields to include
        model = Supplier
        fields = ['name', 'address']

    # Custom validation for the 'name' field
    def clean_name(self):
        # Get the cleaned data for the 'name' field
        name = self.cleaned_data.get('name')

        # Check if the 'name' field is empty
        if not name:
            raise forms.ValidationError('This field is required')

        # Check if a Supplier with the same name already exists
        for instance in Supplier.objects.all():
            if instance.name == name:
                raise forms.ValidationError(name + ' is already created')

        # Return the cleaned 'name' data
        return name

    # Another custom validation for the 'name' field to transform it to uppercase
    def clean_name(self):
        # Get the cleaned 'name' data
        name = self.cleaned_data['name']

        # Transform the 'name' to uppercase
        return name.upper()

    # Custom cleaning for the 'address' field to transform it to uppercase
    def clean_address(self):
        # Get the cleaned 'address' data
        address = self.cleaned_data['address']

        # Transform the 'address' to uppercase
        return address.upper()
    
class SupplierUpdateForm(forms.ModelForm):
    class Meta:
        # Define the metadata for the form, specifying the model and fields to include
        model = Supplier
        fields = ['name', 'address']


# this form use to addmotor html
class MotorForm(forms.ModelForm):
    class Meta:
        # Define the metadata for the form, specifying the model and fields to include
        model = Motor
        fields = ['brand', 'model', 'frame_start', 'engine_start']

    def clean(self):
        # Override the clean method to add custom validation rules for the entire form
        cleaned_data = super().clean()

        # Retrieve data for validation
        brand = cleaned_data.get('brand')
        model = cleaned_data.get('model')
        frame_start = cleaned_data.get('frame_start')
        engine_start = cleaned_data.get('engine_start')

        # Validate that required fields are not empty
        if not brand:
            self.add_error('brand', 'Brand is required.')

        if not model:
            self.add_error('model', 'Model is required.')

        if not frame_start:
            self.add_error('frame_start', 'Frame Start is required.')
        
        if not engine_start:
            self.add_error('engine_start', 'Engine Start is required.')

    def clean_model(self):
        # Additional cleaning for the 'model' field, converting it to uppercase
        model = self.cleaned_data['model']
        return model.upper()
    
    def clean_frame_start(self):
        # Additional cleaning for the 'frame_start' field, converting it to uppercase
        frame_start = self.cleaned_data['frame_start']
        return frame_start.upper()

    def clean_engine_start(self):
        # Additional cleaning for the 'engine_start' field, converting it to uppercase
        engine_start = self.cleaned_data['engine_start']
        return engine_start.upper()

class MotorUpdateForm(forms.ModelForm):
    class Meta:
        # Define the metadata for the form, specifying the model and fields to include
        model = Motor
        fields = ['brand', 'model', 'frame_start', 'engine_start']


# this form use to addreceive, addinventory and delivery in button in inventory html
class ReceiveForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # Extract 'brand' from kwargs (if provided) and remove it from kwargs
        brand = kwargs.pop('brand', None)
        
        # Call the parent class's constructor
        super(ReceiveForm, self).__init__(*args, **kwargs)
        
        # Set the 'readonly' attribute for the 'branch' field to True
        self.fields['branch'].widget.attrs['readonly'] = True

    class Meta:
        # Define the metadata for the form, specifying the model and fields to include
        model = Receive
        fields = ['branch', 'RR_number', 'PO_number', 'supplier', 'delivery_date', 'terms']
        
        # Specify additional widgets for specific fields
        widgets = {
            'delivery_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        # Call the parent class's clean method to perform the default cleaning
        cleaned_data = super().clean()

        # Access cleaned data for specific fields
        RR_number = cleaned_data.get('RR_number')
        PO_number = cleaned_data.get('PO_number')
        supplier = cleaned_data.get('supplier')
        delivery_date = cleaned_data.get('delivery_date')
        terms = cleaned_data.get('terms')

        # Validate the values and add errors if necessary
        if not RR_number:
            self.add_error('RR_number', 'RR Number is required.')

        if not PO_number:
            self.add_error('PO_number', 'PO Number is required.')

        if not supplier:
            self.add_error('supplier', 'Supplier is required.')
        
        if not delivery_date:
            self.add_error('delivery_date', 'Delivery Date is required.')

        if not terms:
            self.add_error('terms', 'Terms is required.')

class ReceiveUpdateForm(forms.ModelForm):
    class Meta:
        # Define the metadata for the form, specifying the model and fields to include
        model = Receive
        fields = ['RR_number', 'PO_number', 'supplier', 'STS_number', 'delivery_date', 'terms']

class InventoryForm(forms.ModelForm):
    # Define a ModelChoiceField for the 'motor' field with an initial empty queryset
    motor = forms.ModelChoiceField(
        queryset=None, required=False, label='Motor'
    )

    def __init__(self, *args, **kwargs):
        # Get the 'brand' from the kwargs
        brand = kwargs.pop('brand', None)
        super(InventoryForm, self).__init__(*args, **kwargs)
        
        # Filter the motor choices based on the selected brand
        if brand:
            self.fields['motor'].queryset = Motor.objects.filter(brand=brand)
        else:
            self.fields['motor'].queryset = Motor.objects.none()

        # Make specific fields read-only
        self.fields['receive'].widget.attrs['readonly'] = True
        self.fields['branch'].widget.attrs['readonly'] = True

    class Meta:
        # Define the metadata for the form, specifying the model and fields to include
        model = Inventory
        fields = ['branch', 'receive', 'motor', 'motor_color', 'frame_number', 'engine_number']

    def clean(self):
        # Clean method for additional validation rules
        cleaned_data = super().clean()

        # Extract cleaned data for validation
        motor = cleaned_data.get('motor')
        motor_color = cleaned_data.get('motor_color')
        frame_number = cleaned_data.get('frame_number')
        engine_number = cleaned_data.get('engine_number')

        # Check if required fields are not provided
        if not motor:
            self.add_error('motor', 'Motor is required.')

        if not motor_color:
            self.add_error('motor_color', 'Motor Color is required.')

        if not frame_number:
            self.add_error('frame_number', 'Frame Number is required.')

        if not engine_number:
            self.add_error('engine_number', 'Engine Number is required.')

    def save(self, commit=True):
        # Custom save method to add additional processing before saving
        instance = super(InventoryForm, self).save(commit=False)

        # Auto-fill the 'status' field with the ID of "BRAND NEW" (which is 1)
        status_brand_new = Status.objects.get(pk=1)
        instance.status = status_brand_new

        # Concatenate the 'frame_start' with the 'frame_number' and set it as 'frame_number'
        if instance.motor:
            instance.frame_number = f"{instance.motor.frame_start} {instance.frame_number}"

        # Concatenate the 'engine_start' with the 'engine_number' and set it as 'engine_number'
        if instance.motor:
            instance.engine_number = f"{instance.motor.engine_start} {instance.engine_number}"

        if commit:
            instance.save()

        return instance

class InventoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['receive', 'motor_color', 'frame_number', 'engine_number']

    def __init__(self, user_branch, *args, **kwargs):
        super(InventoryUpdateForm, self).__init__(*args, **kwargs)

        # Filter the choices for the 'receive' field based on the user's branch
        self.fields['receive'].queryset = Receive.objects.filter(branch=user_branch)


# this form use to transferin in button in inventory html
class TransferInForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        brand = kwargs.pop('brand', None)  # Get the brand from the kwargs
        super(TransferInForm, self).__init__(*args, **kwargs)
        self.fields['branch'].widget.attrs['readonly'] = True

    class Meta:
        model = Receive
        fields = ['branch','RR_number', 'STS_number', 'delivery_date']
        widgets = {
            'delivery_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
       
        RR_number = cleaned_data.get('RR_number')
        STS_number = cleaned_data.get('STS_number')
        delivery_date = cleaned_data.get('delivery_date')

        if not RR_number:
            self.add_error('RR_number', 'RR Number is required.')

        if not STS_number:
            self.add_error('STS_number', 'STS Number is required.')

        if not delivery_date:
            self.add_error('delivery_date', 'Delivery Date is required.')


# this form use to transferout in button in inventory html
class TransferOutForm(forms.ModelForm):
    # Define a ModelChoiceField for the 'inventory' field
    inventory = forms.ModelChoiceField(
        queryset=Inventory.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    def __init__(self, user, *args, **kwargs):
        # Store the user in the instance
        self.user = user
        super(TransferOutForm, self).__init__(*args, **kwargs)

        # Customize the queryset for the 'inventory' field based on the user's branch
        self.fields['inventory'].queryset = Inventory.objects.filter(branch=user.account.branch, status_id=1)

    class Meta:
        # Define the metadata for the form, specifying the model and fields to include
        model = Transfer
        fields = ['transferto', 'controlnumber', 'transferout_date', 'inventory']

        widgets = {
            'transferout_date': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def clean(self):
        # Clean method for additional validation rules
        cleaned_data = super().clean()

        # Extract cleaned data for validation
        transferto = cleaned_data.get('transferto')
        controlnumber = cleaned_data.get('controlnumber')
        transferout_date = cleaned_data.get('transferout_date')
        inventory = cleaned_data.get('inventory')

        # Check if required fields are not provided
        if not transferto:
            self.add_error('transferto', 'Transfer To is required.')

        if not controlnumber:
            self.add_error('controlnumber', 'Control Number is required.')

        if not transferout_date:
            self.add_error('transferout_date', 'Transfer Out Date is required.')

        if not inventory:
            self.add_error('inventory', 'Inventory is required.')

    def save(self, commit=True):
        # Custom save method to perform additional processing before saving
        instance = super(TransferOutForm, self).save(commit=False)

        # Automatically fill up the 'transferfrom' field with the user's branch
        instance.transferfrom = self.user.account.branch

        # Set the 'status' field to the ID of "PENDING" (which is 5)
        status_pending = Status.objects.get(pk=5)
        instance.status = status_pending

        if commit:
            instance.save()

        return instance


# this form use to update detailes transferout in navbar/transaction/transferout
class TransferOutUpdateForm(forms.ModelForm):
    class Meta:
        # Define the metadata for the form, specifying the model and fields to include
        model = Transfer
        fields = ['transferto', 'controlnumber', 'transferout_date', 'inventory']

    def __init__(self, *args, **kwargs):
        # Extract the 'user' from kwargs, defaulting to None
        user = kwargs.pop('user', None)

        # Call the parent class __init__ method with the remaining arguments
        super(TransferOutUpdateForm, self).__init__(*args, **kwargs)

        # Filter the 'inventory' field queryset based on the user's branch
        if user and user.account and user.account.branch:
            self.fields['inventory'].queryset = Inventory.objects.filter(branch=user.account.branch)



# this form use to addrcustomer, addcomaker, addpayment and delivery in button in inventory html
class CustomerForm(forms.ModelForm):
    
    # Meta class to provide information about the form's model and fields
    class Meta:
        model = Customer  # The model associated with this form
        fields = ['branch', 'last_name', 'first_name', 'middle_name', 'address', 'status', 'phone_number', 'residence_number']
        # The fields to be included in the form

    # Constructor method, called when an instance of the form is created
    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)

        # Set the 'readonly' attribute for the 'branch' field
        self.fields['branch'].widget.attrs['readonly'] = True

        # Get the user from kwargs
        user = kwargs.pop('user', None)
        
        # Check if user has 'branch' attribute and autofill the 'branch' field with user's branch
        if user and hasattr(user, 'branch'):
            self.fields['branch'].initial = user.branch

    # Clean method to perform additional validation and cleaning of form data
    def clean(self):
        cleaned_data = super().clean()  # Call the clean method of the parent class

        # Extract cleaned data for individual fields
        last_name = cleaned_data.get('last_name')
        first_name = cleaned_data.get('first_name')
        middle_name = cleaned_data.get('first_name')  # Typo: should be 'middle_name'
        address = cleaned_data.get('address')
        status = cleaned_data.get('status')
        phone_number = cleaned_data.get('phone_number')
        residence_number = cleaned_data.get('residence_number')

        # Check if required fields are not empty, add errors if they are
        if not last_name:
            self.add_error('last_name', 'Last Name is required.')

        if not first_name:
            self.add_error('first_name', 'First Name is required.')

        if not middle_name:
            self.add_error('middle_name', 'Middle Name is required.')

        if not address:
            self.add_error('address', 'Address is required.')

        if not status:
            self.add_error('status', 'Status is required.')

        if not phone_number:
            self.add_error('phone_number', 'Phone Number is required.')

        if not residence_number:
            self.add_error('residence_number', 'Residence Number is required.')

        # Return the cleaned data after validation
        return cleaned_data

class CustomerUpdateForm(forms.ModelForm):
    
    # Meta class to provide information about the form's model and fields
    class Meta:
        model = Customer  # The model associated with this form
        fields = ['last_name', 'first_name', 'middle_name', 'address', 'status', 'phone_number', 'residence_number']
        # The fields to be included in the form for updating a customer

class CoMakerForm(forms.ModelForm):
    
    # Meta class to provide information about the form's model and fields
    class Meta:
        model = CoMaker  # The model associated with this form
        fields = ['branch', 'last_name', 'first_name', 'middle_name', 'address']
        # The fields to be included in the form for a CoMaker

    # Constructor method, called when an instance of the form is created
    def __init__(self, *args, **kwargs):
        super(CoMakerForm, self).__init__(*args, **kwargs)

        # Set the 'readonly' attribute for the 'branch' field
        self.fields['branch'].widget.attrs['readonly'] = True

        # Get the user from kwargs
        user = kwargs.pop('user', None)
        
        # Check if user has 'branch' attribute and autofill the 'branch' field with user's branch
        if user and hasattr(user, 'branch'):
            self.fields['branch'].initial = user.branch

    # Clean method to perform additional validation and cleaning of form data
    def clean(self):
        cleaned_data = super().clean()  # Call the clean method of the parent class

        # Extract cleaned data for individual fields
        last_name = cleaned_data.get('last_name')
        first_name = cleaned_data.get('first_name')
        middle_name = cleaned_data.get('middle_name')
        address = cleaned_data.get('address')

        # Check if required fields are not empty, add errors if they are
        if not last_name:
            self.add_error('last_name', 'Last Name is required.')

        if not first_name:
            self.add_error('first_name', 'First Name is required.')

        if not middle_name:
            self.add_error('middle_name', 'Middle Name is required.')

        if not address:
            self.add_error('address', 'Address is required.')

        # Return the cleaned data after validation
        return cleaned_data

class CoMakerUpdateForm(forms.ModelForm):
    
    # Meta class to provide information about the form's model and fields
    class Meta:
        model = CoMaker  # The model associated with this form
        fields = ['last_name', 'first_name', 'middle_name', 'address']
        # The fields to be included in the form for updating a CoMaker

class PaymentForm(forms.ModelForm):
    
    # Meta class to provide information about the form's model and fields
    class Meta:
        model = Payment  # The model associated with this form
        fields = ['branch', 'date_release', 'loan_type', 'selling_price', 'down_payment', 'amount_finance', 'terms_of_payment', 
                  'monthly_installment', 'promisory_note', 'discount', 'registration_number', 'OR_number', 'remarks', 
                  'residence_number', 'DPS', 'ROPOA']
        # The fields to be included in the form for a Payment

        # Define widgets to customize the display of form fields
        widgets = {
            'date_release': forms.DateInput(attrs={'type': 'date'}),  # Use a date input widget for 'date_release'
        }

    # Constructor method, called when an instance of the form is created
    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)

        # Set the 'readonly' attribute for the 'branch' field
        self.fields['branch'].widget.attrs['readonly'] = True

        # Get the user from kwargs
        user = kwargs.pop('user', None)
        
        # Check if user has 'branch' attribute and autofill the 'branch' field with user's branch
        if user and hasattr(user, 'branch'):
            self.fields['branch'].initial = user.branch

    # Clean method to perform additional validation and cleaning of form data
    def clean(self):
        cleaned_data = super().clean()  # Call the clean method of the parent class

        # Extract cleaned data for individual fields
        date_release = cleaned_data.get('date_release')
        loan_type = cleaned_data.get('loan_type')
        selling_price = cleaned_data.get('selling_price')
        down_payment = cleaned_data.get('down_payment')
        amount_finance = cleaned_data.get('amount_finance')
        terms_of_payment = cleaned_data.get('terms_of_payment')
        monthly_installment = cleaned_data.get('monthly_installment')
        promisory_note = cleaned_data.get('promisory_note')
        discount = cleaned_data.get('discount')
        registration_number = cleaned_data.get('registration_number')
        OR_number = cleaned_data.get('OR_number')
        remarks = cleaned_data.get('remarks')
        residence_number = cleaned_data.get('residence_number')
        DPS = cleaned_data.get('DPS')
        ROPOA = cleaned_data.get('ROPOA')

        # Check if required fields are not empty, add errors if they are
        if not date_release:
            self.add_error('date_release', 'Date Release is required.')

        if not loan_type:
            self.add_error('loan_type', 'Loan Type is required.')

        if not selling_price:
            self.add_error('selling_price', 'Selling Price is required.')

        if not down_payment:
            self.add_error('down_payment', 'Down Payment is required.')

        if not amount_finance:
            self.add_error('amount_finance', 'Amount Finance is required.')

        if not terms_of_payment:
            self.add_error('terms_of_payment', 'Terms of Payment is required.')

        if not monthly_installment:
            self.add_error('monthly_installment', 'Monthly Installment is required.')

        if not promisory_note:
            self.add_error('promisory_note', 'Promissory Note is required.')

        if not discount:
            self.add_error('discount', 'Discount is required.')

        if not registration_number:
            self.add_error('registration_number', 'Registration Number is required.')

        if not OR_number:
            self.add_error('OR_number', 'OR Number is required.')

        if not remarks:
            self.add_error('remarks', 'Remarks is required.')

        if not residence_number:
            self.add_error('residence_number', 'Residence Number is required.')

        if not DPS:
            self.add_error('DPS', 'DPS is required.')

        if not ROPOA:
            self.add_error('ROPOA', 'ROPOA is required.')

        # Return the cleaned data after validation
        return cleaned_data

class PaymentUpdateForm(forms.ModelForm):
    
    # Meta class to provide information about the form's model and fields
    class Meta:
        model = Payment  # The model associated with this form
        fields = ['date_release', 'loan_type', 'selling_price', 'down_payment', 'amount_finance', 'terms_of_payment', 'monthly_installment', 'promisory_note', 'discount', 'registration_number', 'OR_number', 'remarks', 'residence_number', 'DPS', 'ROPOA']


# this form use to Released in button in inventory html   
class CustomerReleasedForm(forms.ModelForm):
    inventory = forms.ModelChoiceField(
        queryset=Inventory.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    def __init__(self, user, *args, **kwargs):
        self.user = user  # Store the user in the instance
        super(CustomerReleasedForm, self).__init__(*args, **kwargs)

        # Customize the queryset for the inventory field based on the user's branch
        self.fields['customer'].queryset = Customer.objects.filter(branch=user.account.branch)
        self.fields['comaker'].queryset = CoMaker.objects.filter(branch=user.account.branch)
        self.fields['payment'].queryset = Payment.objects.filter(branch=user.account.branch)
        self.fields['inventory'].queryset = Inventory.objects.filter(branch=user.account.branch, status_id=1)  # Filter by status "Brand New"
        self.fields['branch'].widget.attrs['readonly'] = True

    class Meta:
        model = Customer_Released
        fields = ['branch', 'customer', 'comaker', 'payment', 'salestype', 'inventory']

    def clean(self):
        cleaned_data = super().clean()

        # Add your validation rules here
        branch = cleaned_data.get('branch')
        customer = cleaned_data.get('customer')
        comaker = cleaned_data.get('comaker')
        payment = cleaned_data.get('payment')
        salestype = cleaned_data.get('salestype')
        inventory = cleaned_data.get('inventory')

        if not branch:
            self.add_error('branch', 'Branch is required.')

        if not customer:
            self.add_error('customer', 'Customer is required.')

        if not comaker:
            self.add_error('comaker', 'Comaker is required.')
        
        if not payment:
            self.add_error('payment', 'Payment is required.')

        if not salestype:
            self.add_error('salestype', 'Salestype is required.')

        if not inventory:
            self.add_error('inventory', 'Inventory is required.')

    def save(self, commit=True):
        instance = super().save(commit=False)

        instance.inventory.status_id = 2  
        instance.inventory.save()

        if commit:
            instance.save()

        return instance
  
class CustomerReleasedUpdateForm(forms.ModelForm):
    
    # Meta class to provide information about the form's model and fields
    class Meta:
        model = Customer_Released  # The model associated with this form
        fields = ['customer', 'comaker', 'payment', 'salestype', 'inventory']
        # The fields to be included in the form for updating a Customer_Released


# this form use to Repo In in button in inventory html   
class RepoInForm(forms.ModelForm):
    
    # Constructor method, called when an instance of the form is created
    def __init__(self, user, *args, **kwargs):
        self.user = user  # Store the user in the instance
        super(RepoInForm, self).__init__(*args, **kwargs)

        # Customize the queryset for the inventory field based on the user's branch
        self.fields['inventory'].queryset = Inventory.objects.filter(branch=user.account.branch, status_id=2)  # Filter by status "Brand New"
        self.fields['branch'].widget.attrs['readonly'] = True  # Set the 'readonly' attribute for the 'branch' field

    # Meta class to provide information about the form's model and fields
    class Meta:
        model = RepoIn  # The model associated with this form
        fields = ['branch', 'inventory']
        # The fields to be included in the form for creating a RepoIn instance

    # Clean method to perform additional validation and cleaning of form data
    def clean(self):
        cleaned_data = super().clean()

        inventory = cleaned_data.get('inventory')

        # Check if the 'inventory' field is not empty, add an error if it is
        if not inventory:
            self.add_error('inventory', 'Inventory is required.')

    # Save method to customize the saving behavior of the form
    def save(self, commit=True):
        instance = super().save(commit=False)

        # Update the status of the associated inventory to "In Repo"
        instance.inventory.status_id = 3  # Assuming 3 represents the "In Repo" status
        instance.inventory.save()

        # Save the RepoIn instance if commit is True
        if commit:
            instance.save()

        return instance


# this form use to Released in button in inventory html   
class RepoOutForm(forms.ModelForm):

    # Define a custom ModelChoiceField for the 'inventory' field with a specific queryset and widget
    inventory = forms.ModelChoiceField(
        queryset=Inventory.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    # Constructor method, called when an instance of the form is created
    def __init__(self, user, *args, **kwargs):
        self.user = user  # Store the user in the instance
        super(RepoOutForm, self).__init__(*args, **kwargs)

        # Customize the queryset for various fields based on the user's branch
        self.fields['customer'].queryset = Customer.objects.filter(branch=user.account.branch)
        self.fields['comaker'].queryset = CoMaker.objects.filter(branch=user.account.branch)
        self.fields['payment'].queryset = Payment.objects.filter(branch=user.account.branch)
        self.fields['inventory'].queryset = Inventory.objects.filter(branch=user.account.branch, status_id=3)  # Filter by status "In Repo"
        self.fields['branch'].widget.attrs['readonly'] = True  # Set the 'readonly' attribute for the 'branch' field

    # Meta class to provide information about the form's model and fields
    class Meta:
        model = RepoOut  # The model associated with this form
        fields = ['branch', 'customer', 'comaker', 'payment', 'salestype', 'inventory']
        # The fields to be included in the form for creating a RepoOut instance

    # Clean method to perform additional validation and cleaning of form data
    def clean(self):
        cleaned_data = super().clean()

        # Extract cleaned data for individual fields
        branch = cleaned_data.get('branch')
        customer = cleaned_data.get('customer')
        comaker = cleaned_data.get('comaker')
        payment = cleaned_data.get('payment')
        salestype = cleaned_data.get('salestype')
        inventory = cleaned_data.get('inventory')

        # Check if required fields are not empty, add errors if they are
        if not branch:
            self.add_error('branch', 'Branch is required.')

        if not customer:
            self.add_error('customer', 'Customer is required.')

        if not comaker:
            self.add_error('comaker', 'Comaker is required.')
        
        if not payment:
            self.add_error('payment', 'Payment is required.')

        if not salestype:
            self.add_error('salestype', 'Salestype is required.')

        if not inventory:
            self.add_error('inventory', 'Inventory is required.')

    # Save method to customize the saving behavior of the form
    def save(self, commit=True):
        instance = super().save(commit=False)

        # Update the status of the associated inventory to "Out Repo"
        instance.inventory.status_id = 4  # Assuming 4 represents the "Out Repo" status
        instance.inventory.save()

        # Save the RepoOut instance if commit is True
        if commit:
            instance.save()

        return instance
  
class RepoOutUpdateForm(forms.ModelForm):
    class Meta:
        model = RepoOut
        fields = ['customer', 'comaker', 'payment', 'salestype', 'inventory']
