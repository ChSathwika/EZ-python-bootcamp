
#functions

#def is a keyword to create a function 

def greetings():
    return 'hello good morning'
print(greetings())

def greetings(branch):
    return ('hello good morning',branch)
print(greetings('cse'))
print(greetings('it'))
print(greetings('ece'))

def greetings(branch):
    print ('hello good morning',branch)
(greetings('cse'))
(greetings('it'))
(greetings('ece'))

#check wheather the input number is even or odd using functions


def evenodd(n):
   if n%2==0:
     return "even"
   else:
      return"odd"
print(evenodd(3)) 

def evenodd(n):
   if n&2==0:
     return "even"
   else:
      return"odd"
print(evenodd(3))

#print num which are divisible by 4 and 6
#arr=[1,36,9,24,2,12]

def check(arr):
  count=0
  for i in arr:
    if i%4==0&i%6==0:
      count+=1
  return count
arr=[1,36,9,24,2,12]
print(check(arr))

def check(arr):
  count=0
  for i in arr:
    if i%4==0&i%6==0:
      print(i,end=' ')#end is used to print the o/p within one line with spaces
      count+=1
  return count
arr=[1,36,9,24,2,12]#arr=list(map(int,input().split()))->user input of array
print('the count is:',check(arr))

#debug the words
#s='sri devi is engineering college'
#print(s[::-1])->without functions

def check(s):
    #'hello i am going to college'
    a=''
    for i in s:
        a=i+a
    return a 
s='sri devi is engineering college'    
print(check(s))

     
# def string(s):
#    s=s.split()
#    s=reversed(s)#->s=list(reversed(s))-> s becomes reverse list
#    print(s)
#    for i in s:
#        rev=i[::-1]
#        print(rev,end=' ')
# s='sri devi is engineering college'    
# print(string(s))  

