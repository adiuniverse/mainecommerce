from django.urls import path
from . import views
app_name = 'common'
urlpatterns = [
   path('home',views.common_comhome,name='commonhome'),
   path('customerregister',views.common_customerregister,name='customerregister'),
   path('sellerregister',views.common_sellerregister,name='sellerregister'),
   path('customerlogin',views.common_customerlogin,name='customerlogin'),
   path('sellerlogin',views.common_sellerlogin,name='sellerlogin'),
   path('commonmaster',views.common_commonmaster,name='commonmaster'),
   path('check_email',views.check_email,name='check_email'),
  
  
]
