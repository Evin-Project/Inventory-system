from django.urls import path
from . import views

urlpatterns = [
    #this urlpattern use in supplier and addsupplier html
    path('addsuppplier', views.add_supplier, name="addsupplier"),
    path('supplier', views.list_supplier, name="supplier"),
    path('update_supplier/<str:pk>/', views.update_supplier, name="addsupplier"),

    #this urlpattern use in motor and addmotor html
    path('addmotor', views.add_motor, name="addmotor"),
    path('motor', views.list_motor, name="motor"),
    path('update_motor/<str:pk>/', views.update_motor, name="addmotor"),

    #this urlpattern use in receive and addreceive html
    path('receive', views.list_receive, name="receive"),
    path('addreceive', views.add_receive, name="addreceive"),
    path('addinventory/<int:receive_id>/', views.add_inventory, name="addinventory"),
    path('update_receive/<str:pk>/', views.update_receive, name="addreceive"),

    #this urlpattern use in inventory and addreceive html
    path('addinventory', views.add_inventory, name="addinventory"),
    path('inventory', views.list_inventory, name="inventory"),
    path('update_inventory/<str:pk>/', views.update_inventory, name="updateinventory"),

    #this urlpattern use in customer and addcustomer html
    path('customer', views.list_customer, name="customer"),
    path('update_customer/<str:pk>/', views.update_customer, name="addcustomer"),
    path('addcustomer', views.add_customer, name="addcustomer"),

    #this urlpattern use in comaker and addcomaker html
    path('addcomaker', views.add_comaker, name="addcomaker"),
    path('comaker', views.list_comaker, name="comaker"),
    path('update_comaker/<str:pk>/', views.update_comaker, name="addcomaker"),

    #this urlpattern use in payment and addpayment html
    path('addpayment', views.add_payment, name="addpayment"),
    path('payment', views.list_payment, name="payment"),
    path('update_payment/<str:pk>/', views.update_payment, name="addpayment"),

    #this urlpattern use in transferout and addtransferout html
    path('add_transferout', views.add_transferout, name="addtransferout"),
    path('transferout', views.list_transferout, name="transferout"),
    path('update_transferout/<str:pk>/', views.update_transferout, name="addtransferout"),

    #this urlpattern use in transferin and addtransferin html
    path('transferin', views.list_transferin, name="transferin"),
    path('transferin/<int:transfer_id>/', views.transfer, name='transferin'),
    path('addtransferin', views.add_transferin, name="addtransferin"),
    

    #this urlpattern use in customerreleased and addcustomerreleased html
    path('customerreleased', views.list_customer_released, name="customerreleased"),
    path('addcustomerreleased', views.add_customer_released, name="addcustomerreleased"),
    path('update_customer_released/<str:pk>/', views.update_customer_released, name="addcustomerreleased"),


    #this urlpattern use in addrepoin html
    path('addrepoin', views.add_repoin, name="addrepoin"),

    #this urlpattern use in addrepoout html
    path('repoout', views.list_repoout, name="repoout"),
    path('addrepoout', views.add_repoout, name="addrepoout"),
    path('update_repoout/<str:pk>/', views.update_repoout, name="addrepoout"),
]