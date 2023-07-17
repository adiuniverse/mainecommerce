from django.shortcuts import redirect

def auth_customer(func):
    def wrap(request, *args, **Kwargs):
        if 'customer' in request.session:
            return func(request, *args, **Kwargs) 
        else:
            return redirect('common:customerlogin')
    return wrap       
