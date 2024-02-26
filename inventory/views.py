from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import * 
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Inventory
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.utils import timezone
from django.forms import inlineformset_factory

# this function use in use in login html
def login_view(request):
    # Check if the request method is POST
    if request.method == 'POST':
        # Retrieve the entered username and password from the POST data
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate the user with the provided username and password
        user = authenticate(request, username=username, password=password)

        # Check if the authentication was successful
        if user is not None:
            # Log in the user and redirect to the 'inventory' page
            login(request, user)
            return redirect('inventory')
        else:
            # If authentication fails, display a login failure message and redirect to the 'login' page
            messages.success(request, ("Log In Failed"))
            return redirect('login')
    else:
        # If the request method is not POST, render the 'login.html' template
        return render(request, 'login.html', {})
    
def logout_view(request):
    # Log out the currently logged-in user
    logout(request)
    
    # Redirect to the 'login' page after successful logout
    return redirect('login')


# this function use in use in supplier and addsupplier html
def list_supplier(request):
    # Set the title for the page
    title = 'List Of Suppliers'

    # Query all Supplier objects from the database
    queryset = Supplier.objects.all()

    # Create a context dictionary with data to be passed to the template
    context = {
        "title": title,
        "queryset": queryset,
    }

    # Render the 'supplier.html' template with the provided context data
    return render(request, "supplier.html", context)

def update_supplier(request, pk):
    # Retrieve the Supplier object from the database using the provided primary key (pk)
    queryset = Supplier.objects.get(id=pk)

    # Create an instance of the SupplierUpdateForm, passing the retrieved Supplier object
    form = SupplierUpdateForm(instance=queryset)

    # Check if the request method is POST (form submission)
    if request.method == 'POST':
        # Create a form instance with the submitted data and the retrieved Supplier object
        form = SupplierUpdateForm(request.POST, instance=queryset)

        # Check if the form is valid
        if form.is_valid():
            # Save the updated data to the database
            form.save()

            # Redirect to the list of suppliers after a successful update
            return redirect('/supplier')

    # Create a context dictionary with the form data
    context = {
        'form': form
    }

    # Render the 'addsupplier.html' template with the provided context data
    return render(request, 'addsupplier.html', context)

def add_supplier(request):
    # Create an instance of the SupplierForm, either with the submitted POST data or as an empty form
    form = SupplierForm(request.POST or None)

    # Check if the form is valid
    if form.is_valid():
        # Save the form data to the database
        form.save()

        # Redirect to the list of suppliers after a successful addition
        return redirect('/supplier')

    # Create a context dictionary with the form and title data
    context = {
        "form": form,
        "title": "Add Supplier"
    }

    # Render the 'addsupplier.html' template with the provided context data
    return render(request, "addsupplier.html", context)


# this function use in use in motor and addmotor html
def update_motor(request, pk):
    # Retrieve the specific Motor instance from the database using the provided primary key (pk)
    queryset = Motor.objects.get(id=pk)

    # Create an instance of the MotorUpdateForm, pre-populated with the data from the retrieved Motor instance
    form = MotorUpdateForm(instance=queryset)

    # Check if the request method is POST (form submission)
    if request.method == 'POST':
        # Create a new instance of MotorUpdateForm with the POST data and the retrieved Motor instance
        form = MotorUpdateForm(request.POST, instance=queryset)

        # Check if the submitted form is valid
        if form.is_valid():
            # Save the updated form data to the database
            form.save()

            # Redirect to the list of motors after a successful update
            return redirect('/motor')

    # Create a context dictionary with the form data
    context = {
        'form': form
    }

    # Render the 'addmotor.html' template with the provided context data
    return render(request, 'addmotor.html', context)

def list_motor(request):
    # Define the title for the page
    title = 'List Of Motors'

    # Retrieve all Motor instances from the database
    queryset = Motor.objects.all()

    # Create a context dictionary with the title and the queryset of motors
    context = {
        "title": title,
        "queryset": queryset,
    }

    # Render the 'motor.html' template with the provided context data
    return render(request, "motor.html", context)

def add_motor(request):
    # Create an instance of MotorForm with POST data from the request
    form = MotorForm(request.POST or None)

    # Check if the form is valid (data passed validation rules)
    if form.is_valid():
        # Save the form data to the database
        form.save()

        # Redirect to the 'list_motor' view after successfully adding a motor
        return redirect('/motor')

    # Create a context dictionary with the form and title
    context = {
        "form": form,
        "title": "Add Motor",
    }

    # Render the 'addmotor.html' template with the provided context data
    return render(request, "addmotor.html", context)


# this function use in use in receive and addreceive html
def add_receive(request):
    # Check if the request method is POST (form submission)
    if request.method == 'POST':
        # Create an instance of ReceiveForm with POST data from the request
        form = ReceiveForm(request.POST)

        # Check if the form is valid (data passed validation rules)
        if form.is_valid():
            # Save the form data to the database and get the receive instance
            receive = form.save()

            # Redirect to the 'addinventory' view, passing the receive_id as a parameter
            return redirect('addinventory', receive_id=receive.id)
    else:
        # If the request method is not POST, create an unbound form with initial data
        # Set the 'branch' field to the current user's branch as a default value
        form = ReceiveForm(initial={'branch': request.user.account.branch})

    # Create a context dictionary with the form and the title
    context = {
        "form": form,
        "title": "Add Receive",
    }

    # Render the 'addreceive.html' template with the provided context data
    return render(request, "addreceive.html", context)

def list_receive(request):
    # Set the title for the HTML page
    title = 'List Of Receive'

    # Retrieve all instances of the Receive model from the database
    queryset = Receive.objects.all()

    # Create a context dictionary with the title and the queryset (list of receives)
    context = {
        "title": title,
        "queryset": queryset,
    }

    # Render the 'receive.html' template with the provided context data
    return render(request, "receive.html", context)

def update_receive(request, pk):
    # Retrieve the specific Receive instance from the database based on the provided primary key (pk)
    queryset = Receive.objects.get(id=pk)

    # Create an instance of the ReceiveUpdateForm, pre-filled with the data from the retrieved instance
    form = ReceiveUpdateForm(instance=queryset)

    # Check if the HTTP request method is POST (indicating form submission)
    if request.method == 'POST':
        # Create a form instance with the data from the POST request and the existing instance
        form = ReceiveUpdateForm(request.POST, instance=queryset)

        # Check if the form is valid
        if form.is_valid():
            # Save the updated data to the database
            form.save()

            # Redirect to the 'list_receive' page after successful update
            return redirect('/receive')

    # Create a context dictionary with the form instance
    context = {
        'form': form
    }

    # Render the 'addreceive.html' template with the provided context data
    return render(request, 'addreceive.html', context)


# this function use in use in inventory and addinventory html
def add_inventory(request, receive_id):
    # Retrieve the specific Receive instance from the database based on the provided receive_id
    receive = Receive.objects.get(pk=receive_id)

    # Extract the brand information from the receive instance
    brand = receive.supplier

    # Check if the HTTP request method is POST (indicating form submission)
    if request.method == 'POST':
        # Create an instance of the InventoryForm, passing the brand information to the form
        form = InventoryForm(request.POST, brand=brand)

        # Check if the form is valid
        if form.is_valid():
            # Save the form data to the database
            form.save()

            # Check if the 'add_another' button is in the POST data
            if 'add_another' in request.POST:
                # Redirect to the 'addinventory' page for the same receive entry
                return redirect('addinventory', receive_id=receive.id)
            # Check if the 'done' button is in the POST data
            elif 'done' in request.POST:
                # Redirect to the 'inventory' page after completing the inventory addition
                return redirect('inventory')

    else:
        # If the request method is not POST, create an instance of the InventoryForm with initial data
        form = InventoryForm(initial={'receive': receive, 'branch': request.user.account.branch}, brand=brand)

    # Create a context dictionary with the receive instance, form, and a title
    context = {
        "receive": receive,
        "form": form,
        "title": "Add Inventory"
    }

    # Render the 'addinventory.html' template with the provided context data
    return render(request, "addinventory.html", context)

def update_inventory(request, pk):
    # Retrieve the specific Inventory instance from the database based on the provided pk (primary key)
    inventory_instance = Inventory.objects.get(id=pk)

    # Retrieve the user's branch information (Assuming user's branch is accessible through the user's account)
    user_branch = request.user.account.branch

    # Create an instance of the InventoryUpdateForm, passing the user's branch and inventory instance to the form
    form = InventoryUpdateForm(user_branch, instance=inventory_instance)

    # Check if the HTTP request method is POST (indicating form submission)
    if request.method == 'POST':
        # Create a new instance of the InventoryUpdateForm with user's branch, form data, and inventory instance
        form = InventoryUpdateForm(user_branch, request.POST, instance=inventory_instance)

        # Check if the form is valid
        if form.is_valid():
            # Save the updated form data to the database
            form.save()

            # Redirect to the 'inventory' page after successfully updating the inventory entry
            return redirect('inventory')

    # Create a context dictionary with the form
    context = {
        'form': form,
    }

    # Render the 'updateinventory.html' template with the provided context data
    return render(request, 'updateinventory.html', context)

def list_inventory(request):
    # Retrieve the branch associated with the current user from the user's account
    branch_to_filter = request.user.account.branch

    # Filter inventory records based on the retrieved branch and specific status_id values
    # Assuming 'status_id' is a field in the 'Inventory' model, and filtering for status_id values 1 and 3
    filtered_records = Inventory.objects.filter(branch=branch_to_filter, status_id__in=[1, 3])

    # Render the 'inventory.html' template with the filtered inventory records as context data
    return render(request, 'inventory.html', {'filtered_records': filtered_records})


# this function use in use in customer and addcustomer html
def add_customer(request):
    # Check if the request method is POST (indicating form submission)
    if request.method == 'POST':
        # Create a CustomerForm instance with the data from the POST request
        form = CustomerForm(request.POST)
        
        # Check if the form is valid
        if form.is_valid():
            # Save the form data to the database
            form.save()
            
            # Redirect to the 'addcustomerreleased' page after successfully adding a customer
            return redirect('addcustomerreleased')
    
    # If the request method is not POST, create an instance of CustomerForm with initial data
    else:
        form = CustomerForm(initial={'branch': request.user.account.branch})
    
    # Create a context dictionary with the form and a title
    context = {
        "form": form,
        "title": "Add Customer"
    }
    
    # Render the 'addcustomer.html' template with the provided context data
    return render(request, "addcustomer.html", context)

def list_customer(request):
    # Get the branch associated with the current user from the request
    branch_to_filter = request.user.account.branch
    
    # Filter customer records based on the user's branch
    filtered_records = Customer.objects.filter(branch=branch_to_filter)

    # Render the 'customer.html' template with the filtered customer records
    return render(request, 'customer.html', {'filtered_records': filtered_records})

def update_customer(request, pk):
    # Get the customer instance to be updated based on the provided primary key (pk)
    queryset = Customer.objects.get(id=pk)
    
    # Create an instance of the 'CustomerUpdateForm' with the data from the retrieved customer instance
    form = CustomerUpdateForm(instance=queryset)
    
    # Check if the request method is POST (form submission)
    if request.method == 'POST':
        # Create a form instance with the submitted POST data and the retrieved customer instance
        form = CustomerUpdateForm(request.POST, instance=queryset)
        
        # Check if the form is valid
        if form.is_valid():
            # Save the updated data to the database
            form.save()
            
            # Redirect to the 'customer' view after successful update
            return redirect('customer')
    
    # Prepare the context data to be passed to the template
    context = {
        'form': form
    }
    
    # Render the 'updatecustomer.html' template with the form and other context data
    return render(request, 'updatecustomer.html', context)


# this function use in use in comaker and addcomaker html
def add_comaker(request):
    if request.method == 'POST':
        form = CoMakerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addcustomerreleased')
    else:
        form = CustomerForm(initial={'branch': request.user.account.branch})
    context = {
        "form": form,
        "title": "Add Customer"
    }
    return render(request, "addcomaker.html", context)

def list_comaker(request):
    # Get the branch associated with the current user from the request
    branch_to_filter = request.user.account.branch
    
    # Filter comaker records based on the user's branch
    filtered_records = CoMaker.objects.filter(branch=branch_to_filter)

    # Render the 'comaker.html' template with the filtered comaker records
    return render(request, 'comaker.html', {'filtered_records': filtered_records})

def update_comaker(request, pk):
    # Get the co-maker instance to be updated based on the provided primary key (pk)
    queryset = CoMaker.objects.get(id=pk)
    
    # Create an instance of the 'CoMakerUpdateForm' with the data from the retrieved co-maker instance
    form = CoMakerUpdateForm(instance=queryset)
    
    # Check if the request method is POST (form submission)
    if request.method == 'POST':
        # Create a form instance with the submitted POST data and the retrieved co-maker instance
        form = CoMakerUpdateForm(request.POST, instance=queryset)
        
        # Check if the form is valid
        if form.is_valid():
            # Save the updated data to the database
            form.save()
            
            # Redirect to the 'comaker' view after successful update
            return redirect('comaker')
    
    # Prepare the context data to be passed to the template
    context = {
        'form': form
    }
    
    # Render the 'updatecomaker.html' template with the form and other context data
    return render(request, 'updatecomaker.html', context)


# this function use in use in payment and addpayment html
def add_payment(request):
    # Check if the request method is POST (form submission)
    if request.method == 'POST':
        # Create a form instance with the submitted POST data
        form = PaymentForm(request.POST)
        
        # Check if the form is valid
        if form.is_valid():
            # Save the form data to the database
            form.save()
            
            # Redirect to the 'addcustomerreleased' view after successful form submission
            return redirect('addcustomerreleased')
    
    # If the request method is not POST (initial page load), create a form instance with initial data
    else:
        form = PaymentForm(initial={'branch': request.user.account.branch})
    
    # Prepare the context data to be passed to the template
    context = {
        "form": form,
        "title": "Add Payment"  # Assuming this title is used in the template
    }
    
    # Render the 'addpayment.html' template with the form and other context data
    return render(request, "addpayment.html", context)

def list_payment(request):
    # Get the branch associated with the current user from the request
    branch_to_filter = request.user.account.branch
    
    # Filter payment records based on the user's branch
    filtered_records = Payment.objects.filter(branch=branch_to_filter)

    # Render the 'payment.html' template with the filtered payment records
    return render(request, 'payment.html', {'filtered_records': filtered_records})

def update_payment(request, pk):
    # Get the payment instance with the given primary key (pk) from the database
    queryset = Payment.objects.get(id=pk)
    
    # Create a form instance with the data from the retrieved payment instance
    form = PaymentUpdateForm(instance=queryset)
    
    # Check if the request method is POST (form submission)
    if request.method == 'POST':
        # Create a form instance with the submitted POST data and the instance to update
        form = PaymentUpdateForm(request.POST, instance=queryset)
        
        # Check if the form is valid
        if form.is_valid():
            # Save the form data to update the payment information in the database
            form.save()
            
            # Redirect to the 'payment' view after successful form submission
            return redirect('payment')
    
    # Prepare the context data to be passed to the template
    context = {
        'form': form
    }
    
    # Render the 'updatepayment.html' template with the form and other context data
    return render(request, 'updatepayment.html', context)


# this function use in use in transferout and addtransferout html
def add_transferout(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        try:
            # Try to get the branch associated with the user's account
            branch_to_filter = request.user.account.branch
        except AttributeError:
            # If there's an AttributeError (e.g., user has no associated account), set branch_to_filter to None
            branch_to_filter = None
    else:
        # If the user is not authenticated, set branch_to_filter to None
        branch_to_filter = None

    # Check if the request method is POST (form submission)
    if request.method == "POST":
        # Create a TransferOutForm instance with the user and POST data
        form = TransferOutForm(request.user, request.POST)
        
        # Check if the form is valid
        if form.is_valid():
            # Save the form data to create a new transfer-out record (commit=False prevents saving until further modification)
            transfer_out = form.save(commit=False)
            
            # Save the transfer-out record to the database
            transfer_out.save()
            
            # Redirect to the 'inventory' view (Replace 'inventory' with the actual URL name)
            return redirect('inventory')
    else:
        # If the request method is not POST (GET request), initialize the form based on the user's authentication status
        if request.user.is_authenticated:
            # If authenticated, create the form with the user as an argument
            form = TransferOutForm(request.user)
        else:
            # If not authenticated, initialize the form without any arguments
            form = TransferOutForm()

    # Prepare the context data to be passed to the template
    context = {
        "form": form,
        "title": "Add Transfer Out",
    }

    # Render the 'addtransferout.html' template with the form and other context data
    return render(request, "addtransferout.html", context)

def update_transferout(request, pk):
    # Get the current user
    user = request.user

    # Retrieve the transfer-out record to be updated using the provided primary key (pk)
    queryset = Transfer.objects.get(id=pk)

    # Create a TransferOutUpdateForm instance with the transfer-out record and the user
    form = TransferOutUpdateForm(instance=queryset, user=user)

    # Check if the request method is POST (form submission)
    if request.method == 'POST':
        # Create a TransferOutUpdateForm instance with the POST data, transfer-out record, and the user
        form = TransferOutUpdateForm(request.POST, instance=queryset, user=user)

        # Check if the form is valid
        if form.is_valid():
            # Save the updated form data to the transfer-out record
            form.save()

            # Redirect to the 'transferout' view
            return redirect('/transferout')

    # Prepare the context data to be passed to the template
    context = {
        'form': form
    }

    # Render the 'addtransferout.html' template with the form and other context data
    return render(request, 'addtransferout.html', context)

def list_transferout(request):
    # Set the title for the page
    title = 'List Of TransferOut'

    # Get the user's branch from the account associated with the current user
    user_branch = request.user.account.branch  # Assuming user's branch is accessible this way

    # Filter the queryset to include TransferOut objects with 'transferfrom' matching the user's branch and status equal to 5
    # Note: Adjust the field names and values according to your actual model structure
    queryset = Transfer.objects.filter(transferfrom=user_branch, status=5)

    # Prepare the context data to be passed to the template
    context = {
        "title": title,
        "queryset": queryset
    }

    # Render the 'transferout.html' template with the context data, and the resulting HTML is sent as the HTTP response
    return render(request, "transferout.html", context)


# this function use in use in transferin and addtransferin html
def list_transferin(request):
    # Set the title for the page
    title = 'List Of TransferIn'

    # Get the user's branch from the account associated with the current user
    user_branch = request.user.account.branch  # Assuming user's branch is accessible this way

    # Filter the queryset to include TransferIn objects with 'transferto' matching the user's branch
    # Note: Adjust the field names according to your actual model structure
    queryset = Transfer.objects.filter(transferto=user_branch, status_id=5)

    # Prepare the context data to be passed to the template
    context = {
        "title": title,
        "queryset": queryset
    }

    # Render the 'transferin.html' template with the context data, and the resulting HTML is sent as the HTTP response
    return render(request, "transferin.html", context)

def transfer(request, transfer_id):
    # Retrieve the Transfer object using the provided transfer_id
    transfer = Transfer.objects.get(pk=transfer_id)

    # Create a TransferInForm instance using the data from the related Inventory's Receive record
    form = TransferInForm(instance=transfer.inventory.receive)

    # Check if the request method is POST (i.e., form submission)
    if request.method == 'POST':
        # Check if the 'accept_button' is present in the POST data
        if 'accept_button' in request.POST:
            # Get the user's branch from the request
            user_branch = request.user.account.branch
            
            # Update Transfer details upon accepting the transfer
            transfer.transferin_date = timezone.now().date()
            transfer.status_id = 6  # Assuming 6 represents the 'Accepted' status
            transfer.save()

            # Update the branch of the transferred inventory to the user's branch
            transfer.inventory.branch = user_branch
            transfer.inventory.save()

            # Redirect to the 'transferin' page after processing the transfer
            return redirect('transferin')

    # Prepare the context with the TransferInForm for rendering the template
    context = {
        'form': form
    }

    # Render the 'addtransferin.html' template with the provided context
    return render(request, 'addtransferin.html', context)

def add_transferin(request):
    # Check if the request method is POST (i.e., form submission)
    if request.method == 'POST':
        # Create a TransferInForm instance with the data from the POST request
        form = TransferInForm(request.POST)
        
        # Check if the form is valid
        if form.is_valid():
            # Save the form data to the database
            form.save()
            
            # Redirect to the 'inventory' page after successfully adding a transfer in record
            return redirect('inventory')
    else:
        # If the request method is not POST, create an instance of TransferInForm with initial data
        # Set the 'branch' field to the user's branch obtained from the request
        form = TransferInForm(initial={'branch': request.user.account.branch})

    # Prepare the context with the TransferInForm and a title for rendering the template
    context = {
        "form": form,
        "title": "Transfer In",
    }
    
    # Render the 'addtransferin.html' template with the provided context and form
    return render(request, "addtransferin.html", context)


# this function use in use in customerreleased and addcustomerreleased html
def add_customer_released(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        try:
            # Try to get the user's branch from the account
            branch_to_filter = request.user.account.branch
        except AttributeError:
            # If the user does not have an account or branch, set branch_to_filter to None
            branch_to_filter = None
    else:
        # If the user is not authenticated, set branch_to_filter to None
        branch_to_filter = None

    # Check if the request method is POST (i.e., form submission)
    if request.method == 'POST':
        # Create a CustomerReleasedForm instance with the user and data from the POST request
        form = CustomerReleasedForm(request.user, request.POST)
        
        # Check if the form is valid
        if form.is_valid():
            # Save the form data to the database
            customer_released = form.save(commit=False)
            customer_released.save()
            
            # Redirect to the 'customerreleased' page after successfully adding a customer released record
            return redirect('customerreleased')  # Redirect to a success page
    else:
        # If the request method is not POST, create an instance of CustomerReleasedForm
        if request.user.is_authenticated:
            # If the user is authenticated, set initial data including branch and status
            form = CustomerReleasedForm(request.user, initial={'branch': request.user.account.branch, 'status': Status.objects.get(pk=1)})
        else:
            # If the user is not authenticated, create an instance of CustomerReleasedForm without initial data
            form = CustomerReleasedForm()

    # Render the 'addcustomerreleased.html' template with the form
    return render(request, 'addcustomerreleased.html', {'form': form})

def list_customer_released(request):
    # Get the branch associated with the current user from the request
    branch_to_filter = request.user.account.branch
    
    # Filter payment records based on the user's branch
    filtered_records = Customer_Released.objects.filter(branch=branch_to_filter)

    # Render the 'payment.html' template with the filtered payment records
    return render(request, 'customerreleased.html', {'filtered_records': filtered_records})

def update_customer_released(request, pk):
    # Retrieve the existing Customer_Released instance from the database using the provided primary key (pk)
    queryset = Customer_Released.objects.get(id=pk)
    
    # Create a form instance with the retrieved Customer_Released instance as the initial data
    form = CustomerReleasedUpdateForm(instance=queryset)

    # Check if the request method is POST (i.e., form submission)
    if request.method == 'POST':
        # Create a CustomerReleasedUpdateForm instance with the data from the POST request and the existing instance
        form = CustomerReleasedUpdateForm(request.POST, instance=queryset)
        
        # Check if the form is valid
        if form.is_valid():
            # Save the updated form data to the database
            form.save()
            
            # Redirect to the 'customerreleased' page after successfully updating the customer released record
            return redirect('customerreleased')

    # If the request method is not POST or the form is not valid, prepare the context for rendering the template
    context = {
        'form': form
    }

    # Render the 'addcustomerreleased.html' template with the form for updating the customer released record
    return render(request, 'addcustomerreleased.html', context)


# this function use in use in customerreleased and addcustomerreleased html
def add_repoin(request):
    # Check if the request method is POST (i.e., form submission)
    if request.method == 'POST':
        # Create a RepoInForm instance with the data from the POST request and the current user
        form = RepoInForm(request.user, request.POST)
        
        # Check if the form is valid
        if form.is_valid():
            # Save the form data to the database
            form.save()
            
            # Redirect to the 'inventory' page after successfully adding a repo in record
            return redirect('inventory')

    # If the request method is not POST, create a RepoInForm instance with the current user and initial data
    else:
        form = RepoInForm(user=request.user, initial={'branch': request.user.account.branch})

    # Prepare the context for rendering the template
    context = {
        "form": form,
        "title": "Add Customer"
    }

    # Render the 'addrepoin.html' template with the form for adding a repo in record
    return render(request, "addrepoin.html", context)


# this function use in use in customerreleased and add_repoout html
def add_repoout(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        try:
            # Attempt to get the branch information from the user's account
            branch_to_filter = request.user.account.branch
        except AttributeError:
            # Set branch_to_filter to None if the user's account doesn't have a branch attribute
            branch_to_filter = None
    else:
        # Set branch_to_filter to None if the user is not authenticated
        branch_to_filter = None

    # Check if the request method is POST (i.e., form submission)
    if request.method == 'POST':
        # Create a RepoOutForm instance with the data from the POST request and the current user
        form = RepoOutForm(request.user, request.POST)
        
        # Check if the form is valid
        if form.is_valid():
            # Save the form data to the database (commit=False prevents saving until additional processing)
            repoout = form.save(commit=False)
            repoout.save()
            
            # Redirect to the 'repoout' page after successfully adding a repo out record
            return redirect('repoout')  # Redirect to a success page

    # If the request method is not POST, create a RepoOutForm instance with the current user and initial data
    else:
        # Check if the user is authenticated
        if request.user.is_authenticated:
            # Create the form with initial data, including the user's branch and a default status
            form = RepoOutForm(request.user, initial={'branch': request.user.account.branch, 'status': Status.objects.get(pk=1)})
        else:
            # Create the form without initial data for an unauthenticated user
            form = RepoOutForm()

    # Prepare the context for rendering the template
    context = {
        "form": form
    }

    # Render the 'addrepoout.html' template with the form for adding a repo out record
    return render(request, 'addrepoout.html', context)

def list_repoout(request):
    # Get the branch associated with the current user
    branch_to_filter = request.user.account.branch

    # Filter RepoOut records based on the user's branch
    filtered_records = RepoOut.objects.filter(branch=branch_to_filter)

    # Render the 'repoout.html' template with the filtered RepoOut records
    return render(request, 'repoout.html', {'filtered_records': filtered_records})

def update_repoout(request, pk):
    # Retrieve the RepoOut object with the given primary key (id)
    queryset = RepoOut.objects.get(id=pk)

    # Create a form instance for updating the RepoOut object
    form = RepoOutUpdateForm(instance=queryset)

    # Check if the form is submitted via POST method
    if request.method == 'POST':
        # Create a form instance with the POST data and the RepoOut object instance
        form = RepoOutUpdateForm(request.POST, instance=queryset)

        # Check if the form is valid
        if form.is_valid():
            # Save the updated RepoOut object to the database
            form.save()

            # Redirect to the 'repoout' page after successful update
            return redirect('repoout')

    # Prepare the context for rendering the template with the form
    context = {
        'form': form
    }

    # Render the 'addrepoout.html' template with the form for updating RepoOut
    return render(request, 'addrepoout.html', context)

