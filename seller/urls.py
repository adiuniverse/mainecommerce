from django.urls import path,include
from . import views
app_name = 'seller'
urlpatterns = [
   path('sellerhome',views.seller_sellerhome,name='sellerhome'),
   path('catalogue',views.seller_catalogue,name='catalogue'),
   path('addproduct',views.seller_addproduct,name='addproduct'),
   path('updatestock',views.seller_updatestock,name='updatestock'),
   path('getstock', views.get_stock, name='getstock'),
   path('sellerchangepassword',views.seller_sellerchangepassword,name='sellerchangepassword'),
   path('recentorder',views.seller_recentorder,name='recentorder'),
   path('orderhistory',views.seller_orderhistory,name='orderhistory'),
   path('sellerprofile',views.seller_sellerprofile,name='sellerprofile'),
   path('sellermaster',views.seller_sellermaster,name='sellermaster'),
   path('sellerlogout',views.sellerlogout,name='sellerlogout'),
  
   
]
