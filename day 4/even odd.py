n=2397
m=3
n=str(n)
#output:592721 if even digit add with m
#odd digit multiply with m
for i in n:
 if int(i) %2==0:
      print(int(i)+m,end='')
 else:
      print(int(i)*m,end='') 

#swap without using 3rd varaible

a=2
b=4
print('before swap',a,b)
a=a-b
b=a+b
a=b-a
print('after swap',a,b)
