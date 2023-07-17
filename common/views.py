from django.shortcuts import render,redirect
from .models import Customer
from .models import Seller
import random
from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse
from .decorator import auth_customer

# Create your views here.
@auth_customer
def common_comhome(request):
    return render(request,'client/comhome.html')
def common_customerregister(request):

    # by default, form method will be get

    if request.method == 'POST':  # when submit button clicked
        c_name  = request.POST['fname'] # to get textbox data 
        c_email = request.POST['email']
        c_address = request.POST['address']
        c_phone = request.POST['phonenumber']
        c_gender = request.POST['gender']
        c_password = request.POST['password']

        # in ORM, if we want to insert a data in table,
        # 1. create an object of model class, here model class is Customer
        new_customer = Customer(customer_name = c_name, email = c_email,
        address = c_address,phone = c_phone,gender = c_gender, password = c_password)
        # call save() method 
        new_customer.save()
       


    return render(request,'client/customerregister.html')    
def common_sellerregister(request):


    if request.method == 'POST':
        s_name = request.POST['fullname']
        s_email = request.POST['email']
        s_address = request.POST['address']
        s_phone = request.POST['phonenumber']
        s_company = request.POST['companyname']
        s_holder = request.POST['holdername']
        s_ifsc = request.POST['ifsc']
        s_branch = request.POST['branch']
        s_account = request.POST['accountnumber']
    
        seller_pic = request.FILES['file']
        user_name = random.randint(1111,9999)
        passwd = 'sel-' + str(user_name) + s_name # result will be sel-7867-john
        new_seller = Seller(seller_name = s_name, email = s_email, address = s_address,
        phone = s_phone, company_name = s_company, accountholder_name = s_holder,
        ifsc = s_ifsc, branch = s_branch, account_number = s_account,seller_pic = seller_pic,user_name=user_name,
        password = passwd)

        new_seller.save()

        message = 'Hi your user name is ' + str(user_name) + ' and password is ' + passwd

        # send_mail function used to send mail through our application
        # 1st arguement -> subject
        # 2nd arguement -> message
        # 3rd arguement -> from email
        # 4th arguement -> recipent list , here recipient list should be in an array format
        send_mail('username and password',
            message,
            settings.EMAIL_HOST_USER,
            [s_email,] 
        )

    return render(request,'client/sellerregister.html')    
def common_customerlogin(request):
    msg = ""  
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']

        try:
           customer = Customer.objects.get(email = email, password = password)
           request.session['customer'] = customer.id
           return redirect('customer:customerhome')
        except Exception as e:
            print(e)
            msg = "Customer Login succsessfully"
    return render(request,'client/customerlogin.html',{'message':msg})    

def common_sellerlogin(request):
    msg = ""
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        # when we use get() to fetch data, we must use try except,
        # if the data is not found in the table, exception will be raised
        try:
            seller = Seller.objects.get(user_name = username, password = password)
            request.session['seller'] = seller.id
            return redirect('seller:sellerhome')
        except Exception as e:
            print(e)
            msg = "UserName or password Incorrect"
            # data from view to html will be passed in render() as dictionary
    return render(request,'client/sellerlogin.html',{'message':msg})    
def common_commonmaster(request):
    return render(request,'client/commonmaster.html')  


def check_email(request):
    email = request.POST['email']

    exist = Customer.objects.filter(email = email).exists()

    return JsonResponse({'status' : exist})