from django.urls import path
from . import views
app_name = 'ecomadmin'
urlpatterns = [
  path('ecomhome',views.ecomadmin_ecomhome,name='ecomhome'),  
  path('viewseller',views.ecomadmin_viewseller,name='viewseller'),  
  path('viewcustomer',views.ecomadmin_viewcustomer,name='viewcustomer'), 
  path('ecommaster',views.ecomadmin_ecommaster,name='ecommaster'),  
  path('delete/<int:sid>',views.delete_sell,name='delete_sell'),
  path('delete/<int:sid>',views.delete_cust,name = 'delete_cust'),
  path('approve/<int:sid>',views.approve,name='approve'),
  
]
