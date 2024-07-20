#exception handling in python


'''difference b/w bug error and exception 
bug - which is not expected 
error-syntax error mistake done while writing the program-during the compile time 
exception- during the run time

if we wont use exception-

keywords
try,except,else,finally'''

a=10
b=0
c=a/b
print(c)

n1=100
n2=200
print(n1+n2)
n1=100
n2=200
print(n1+n2)

try:
    a=10
    b=0
    c=a/b
    print(c)
    n1=100
    n2=200
    print(n1+n2)
except Exception:
    print('divide by zero is not possible')
    n1=100
    n2=200
    print(n1+n2)

try:
    a=10
    print(b)
except NameError:
    print('variable b is not assigned')

try:
    arr=[1,7,8,12,36]
    print(arr[4])#arr[5]-cannot access
except IndexError:
    print('cannot access the index value')
else:
    print('no exception occured')
finally:
    print('finally wed is last day of training') # anyhow finally will get exceuted #where we use finally -