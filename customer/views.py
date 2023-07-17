from django.shortcuts import render,redirect
from seller.models import Product
from . models import Cart
from .models import Customer
from .decorator import auth_customer
# Create your views here.
@auth_customer
def customer_custhome(request):
        print(request.session['customer'])
    # if 'customer' in request.session:
        products = Product.objects.all() # select * from product\
        # products = [
        #  {
    #       seller: 2,
    #       product_name : 'laptop',
    #         description : 'dedfr'
    #         -------

        #   }  ,
        #  {
    #       seller: 2,
    #       product_name : 'laptop',
    #         description : 'dedfr'
    #         -------

        #   } 
        # 
        # ]
        # we pass data from view to html in dictionary format
        return render(request,'like/custhome.html',{'product_list': products})

    # else:
    #     return redirect('common:customerlogin')
@auth_customer
def customer_productdetails(request,pid):
    msg =''
    product_data = Product.objects.get(id = pid) # fetching single data from table

    if request.method == 'POST':
        product_id = request.POST['pid']

        item_exist = Cart.objects.filter(product_id = product_id, customer_id = request.session['customer']).exists()
        
        if not item_exist : # if item_exist == false

            cart_item = Cart(product_id = product_id, customer_id = request.session['customer'])
            cart_item.save()
            return redirect('customer:mycart')
        else :
            msg = 'Item Already in Cart'
    return render(request,'like/productdetails.html',{'product': product_data,'msg':msg})
@auth_customer
def customer_mycart(request):
    product_data = Cart.objects.filter(customer_id = request.session['customer'])
    return render(request,'like/mycart.html',{'cart_list':product_data})        
@auth_customer
def customer_myorder(request):
    return render(request,'like/myorder.html')
@auth_customer    
def customer_custchangepassword(request):
   
    msg=""
    if request.method == 'POST':
        customer = Customer.objects.get(id = request.session['customer'])

        current_pass = request.POST['currentpassword'] 
        new_pass = request.POST['newpassword'] 
        confirm_pass = request.POST['confirm']

        if customer.password == current_pass:

                if new_pass == confirm_pass:
                    customer.password = new_pass
                    customer.save()
                    msg = 'Password changed succesfully'

                else:
                    msg = 'Password does not match'

        else:
                msg = 'Incorrect Password'

 


    return render(request,'like/custchangepassword.html',{'msg':msg})


@auth_customer    
def customer_profilee(request):
    msg = ''
    cust_list = Customer.objects.get(id=request.session['customer'])
    if request.method == 'POST':
        customer = Customer.objects.get(id=request.session['customer'])

        customer_name = request.POST['c_name']
        email_address = request.POST['c_email']
        address = request.POST['c_address']
        phone_number = request.POST['c_number']

        customer.customer_name = customer_name
        customer.email = email_address
        customer.address = address
        customer.phone = phone_number
        customer.save()
        msg = 'Profile updated successfully'
    context = {
        'custs': cust_list,
        'msg': msg
    }
    return render(request,'like/profilee.html',context)



    
def custlogout(request):
    del request.session['customer']
    request.session.flush()
    return redirect('common:customerlogin')
    
   

def customer_customermaster(request):
    return render(request,'like/customermaster.html')


@auth_customer
def delete_cart(request,id):
    cart_item = Cart.objects.get(product = id, customer = request.session['customer'])

    cart_item.delete()

    return redirect('customer:mycart')


def update_cart(request,id):
    cart_item = Cart.objects.get(product = id, customer= request.session['customer'])
    cart_item.price = 250
    cart_item.save()
    return redirect('customer:mycart')


    


      

    