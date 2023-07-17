from django.urls import path
from . import views

app_name = 'customer'

urlpatterns = [
   path('custhome',views.customer_custhome,name='customerhome'), 
   path('productdetails/<int:pid>',views.customer_productdetails,name='productdetails'),
   path('mycart',views.customer_mycart,name='mycart'),
   path('myorder',views.customer_myorder,name='myorder'),
   path('custchangepassword',views.customer_custchangepassword,name='customerchangepassword'),
   path('profilee',views.customer_profilee,name='customerprofile'),
   path('custlogout',views.custlogout,name='custlogout'),
   path('customermaster',views.customer_customermaster,name='customermaster'),
   path('delete/<int:id>',views.delete_cart,name='delete_cart'),
   path('update/<int:id>',views.update_cart,name='update_cart'),
   

]
