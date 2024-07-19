#operators

print(2&1|5)# 10 01 =00  000 101 5 is printed as ouput
print(5 ^ 7) 

'''membership operators 
 
 in,not in
 is ,is not '''

'''s='123ABC$' '''
count=0
for i in s:
  if(not(i.isdigit())):
    count+=1
print(count) 

#how many fruits are present

data=[1,8,'apple','carrot','mango']
fruits=['apple','mango','orange','watermelon']
for i  in data:
  if i in fruits:
       print(i) 
 
data=[1,8,'apple','carrot','mango']
fruits=['apple','mango','orange','watermelon']
vegeis=['tomato','beans','carrot','onions']
for i  in data:
  if i in vegeis and i not in fruits:
       print(i)
 

 #identity operators  true or False

s='hello'
s1='hello sridevi'
print(s in s1)

s='hello'
s1='  hello world  '
print(s not in s1)

s='he is good boy'
print(len(s))

s='he is good boy'
s=s.split()
print(s)
print(len(s))

s='he is good boy he is playing'
s=s.split()

print(s.count ('he'))

n=10
n1=True
print(n and n1) True

n=10
n1=False
print(n and n1) False

n=True
n1=False
print(n or n1) 