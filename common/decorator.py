from django.shortcuts import redirect

def auth_customer(func):
    def wrap(request, *args, **Kwargs):
        if 'customer' in request.session:
            return redirect('customer:custhome')
            # return func(request, *args, **Kwargs) 
        else:
             return func(request, *args, **Kwargs)
    return wrap       
