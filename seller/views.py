from django.shortcuts import render,redirect
from .models import Product
from .models import Seller
from django.http import JsonResponse
# Create your views here.
def seller_sellerhome(request):
    seller_data = Seller.objects.get(id= request.session['seller'])
    return render(request,'frame/sellerhome.html',{'data':seller_data})
def seller_sellermaster(request):
    seller_data = Seller.objects.get(id= request.session['seller'])
    return render(request,'frame/sellermaster.html',{'data':seller_data})
def seller_catalogue(request):
    seller_products = Product.objects.filter(seller = request.session['seller'])
    seller_data = Seller.objects.get(id = request.session['seller'])
    context = {'products':seller_products,
                'data': seller_data,
              }
    return render(request,'frame/catalogue.html',context)
def seller_addproduct(request):
    msg = ""
    if request.method == 'POST':
        p_name = request.POST['productname']
        p_description = request.POST['description']
        p_productnumber = request.POST['productnumber']
        p_stock = request.POST['currentstock']
        p_price = request.POST['price']
        p_image = request.FILES['file']
      
        new_product = Product(product_name = p_name, description = p_description,
        number = p_productnumber, stock = p_stock, price = p_price,image = p_image,
        seller_id = request.session['seller'])
       
        new_product.save()
        
    

        msg = "product added successfully"
    return render(request,'frame/addproduct.html',{'message':msg})



def seller_updatestock(request):
    seller_data = Seller.objects.get(id=request.session['seller'])
    product_data = Product.objects.filter(seller=request.session['seller'])

    if request.method == 'POST':
        new_stock = request.POST['new_stock']
        product_id = request.POST['productid']
        new_price = request.POST['new_price']

        product = Product.objects.get(id=product_id)
        product.current_stock = product.current_stock + int(new_stock)
        product.price = new_price

        product.save()
    context = {'prod_data': product_data,
                    'data': seller_data,
                    }
    return render(request,'frame/updatestock.html',context)




def seller_sellerchangepassword(request):
    

   
    msg=""
    if request.method == 'POST':
        current_pass = request.POST['currentpassword'] 
        new_pass = request.POST['newpassword'] 
        confirm_pass = request.POST['confirm']

        seller = Seller.objects.get(id = request.session['seller'])
       
       

        if seller.password == current_pass:

                if new_pass == confirm_pass:
                    # customer.password = new_pass
                    # customer.save()
                    seller = Seller.objects.filter(id = request.session['seller']).update(password = new_pass)

                    msg = 'Password changed succesfully'

                else:
                    msg = 'Password does not match'

        else:
                msg = 'Incorrect Password'

 



    return render(request,'frame/sellerchangepassword.html',{'msg':msg})
def seller_recentorder(request):
    return render(request,'frame/recentorder.html')
def seller_orderhistory(request):
    return render(request,'frame/orderhistory.html')


def seller_sellerprofile(request):
    msg=''
    seller = Seller.objects.get(id=request.session['seller'])
    if request.method=='POST':
        # seller = Seller.objects.get(id = request.session['seller'])

        seller_name = request.POST['s_name']
        seller_email = request.POST['s_email']
        seller_address = request.POST['s_address']
        seller_number = request.POST['s_phone']
        company_name = request.POST['comp_name']
        accholder = request.POST['accholder_name']
        branch = request.POST['s_branch']
        ifsc = request.POST['s_ifsc']
        seller_image = request.FILES['file']
        acc_number = request.POST['accnum']

        seller.seller_name = seller_name
        seller.email = seller_email
        seller.address = seller_address
        seller.phone = seller_number
        seller.company_name = company_name
        seller.accountholder_name = accholder
        seller.ifsc = ifsc
        seller.branch = branch
        seller.seller_pic = seller_image
        seller.account_number=acc_number
        seller.save()
        msg = 'Profile updated successfully'
    context = {
        'data': seller,
        'msg':msg
    }
    return render(request,'frame/sellerprofile.html',context)    



def sellerlogout(request):
    
    del request.session['seller']
    request.session.flush()
    return redirect('common:sellerlogin')
def get_stock(request):
    id = request.POST['id']
    product =Product.objects.get(id=id)
    product_name = product.product_name
    current_stock = product.current_stock
    price = product.price
    product_id = product.id
    return JsonResponse({'p_name':product_name,'stock':current_stock,'p_id':product_id,'price':price})
    
   
         
