'''
    hàm function
'''


""" def myFunction(msg):
    print(msg)


myFunction('hello') #truyền đối số vị trí

def show_full_name(fname, lname):
    print(f'{fname}, {lname}')

show_full_name('huy', 'la')

def add(x, y=40):
    return x+y

print(add(y=10, x=100))

def func(lst=[]):
    lst.append(2)
    print(lst)

func()
func() """

""" friend = ['bob', 'anna']

def my_func(friend):
    friend = friend + ['joe']
    print(friend) """
""" 
my_func()
 """
""" # lambda
print((lambda x, y: x + y)(1, 2))

# first class function: là 1 hàm nhận vào 1 hàm khác
def greet(msg):
    print('hello ' + msg)

hello = greet
print(hello('jen')) #None la gia tri mac dinh ma ham tra ve

def fnc():
    pass """

""" # *args: collect tất cả đối số vị trí rồi trả về 1 tuple, * là vị trí, ** là đối số có tên
def add(*args):
    print(type(args))
    return sum(args)

print(add(1, 2, 3, 4))
lst = [1, 2, 3, 4]
print(*lst)

lst1 = [3, 10, 4, 5, 6, 7]
first, *mid, last = lst1
print(first)
print(mid)
print(last) """

def add(*lst, operation):
    return operation(lst)

print(add(1, 2, 3, 4, operation=sum))