from django.shortcuts import render,redirect
from common . models import Customer,Seller
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def ecomadmin_ecomhome(request):
    return render(request,'hope/ecomhome.html')
def ecomadmin_ecommaster(request):
    return render(request,'hope/ecommaster.html')  


def ecomadmin_viewseller(request):
    seller_list = Seller.objects.all()
    return render(request,'hope/viewseller.html',{'seller_data':seller_list})  

def ecomadmin_viewcustomer(request):
    customer_list = Customer.objects.all()

    return render(request,'hope/viewcustomer.html',{'customer_data':customer_list})  

def delete_sell(request,sid):
    seller_list = Seller.objects.get(id = sid)
    seller_list.delete()
    return redirect('ecomadmin:viewseller')


def delete_cust(request,sid):
    customer_list = Customer.objects.get(id = sid)
    customer_list.delete()
    return redirect('ecomadmin:viewcustomer')

def approve(request,sid):
    seller=Seller.objects.get(id=sid)
    message = ' Welcome to ECOMMMERCE OFFICIAL SHOPPING WEBSITE you can now login to your account, Thanks you'
    send_mail(
        'Login Approved',
        message,
        settings.EMAIL_HOST_USER,
        [seller.email,], 
    )
    seller.approved=True
    seller.save()
    return redirect('ecomadmin:viewseller')