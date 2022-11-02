def my_Dec (func):
    def wrap_func(*args , **kwargs):
        print('*******')
        func(*args , **kwargs)
        print('*******')
    return wrap_func
@my_Dec
def hello(greeting , emoji = ":("):
    print(greeting , emoji)

hello('Hii' , ':)')
# qw = my_Dec (hello)
# print(qw())
