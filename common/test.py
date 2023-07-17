




def div_dec(func):

    def wrapper(a,b) :
        if b > a :
            a,b = b,a

        return func(a,b)

    return wrapper
@div_dec
def divide(a,b):
    res = a/b
    print(res)

divide(2,10)

