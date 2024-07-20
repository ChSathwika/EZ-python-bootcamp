 
#sum of natural numbers

def sum_of_natural(n):
    if n==1:
        return 1
    else:
        return n+sum_of_natural(n-1)
n=int(input())
print(sum_of_natural(n))

#fibinocci using functions

def fib(n):
    if n==0 or n==1 :
        return n
    else:
        return fib(n-1)+fib(n-2)
n=int(input())
print(fib(n-1))# fib(n)

