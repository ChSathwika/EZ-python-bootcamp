#list is a collection of ordered element 
#operations - insert,delete,update, so -mutable data structure
'''represention-[ ]
syntax:
list_name=[ obj1,obj2,obj3,.....objn]'''

#[operations
mobiles=['iphone','iqoo','oneplus']
print(mobiles)
print(mobiles[1])
print(mobiles[-1])
mobiles.insert(2,'sumsung') #at certain position
mobiles.append('vivo')
print(mobiles)

mobiles.pop(0)
print(mobiles)
mobiles.remove('oneplus')
print(mobiles)

#mobiles.clear()# list elements becomes empty but list would be there
#print(mobiles)

mobiles[1]='googlepixel'
print(mobiles)

mobiles=['iphone','sumsung','vivo']
print(mobiles[True])

mobiles=['iphone','sumsung','vivo']
count=1
for ele in mobiles:
    print(count,ele)
    count+=1
#even positions

'''mobiles=['iphone','sumsung','vivo','oneplus','pixel']
for i in range(0,len(mobiles)):
    if i%2==0:
        print(mobiles[i])'''

#even position reverse 

'''mobiles=['iphone','sumsung','vivo','oneplus','pixel']
for i in range(0,len(mobiles)):
    if i%2==0: #odd !=
        rev=mobiles[i]
        print(rev[::-1])

    else:
        print(mobiles[i])'''


arr=[1,2,3,4,5]
k=3
#[3,4,5,1,2]

first=arr[k-1:]
second=arr[:k-1]
print(first+second)
first.extend(second)#without using concatenation
print(first) 

arr=[1,2,3,4,5]
k=3
#[5,4,3,1,2]

first=arr[k+1:k-(k-1):-1]
second=arr[:k-1]
print(first+second)


arr=[1,2,3,4,5]
k=3
#[5,4,1,2,3]
first=arr[k-1:k-(k-2):-1]
print(first)


mobiles=['iphone','sumsung','vivo','oppo','iqoo']
del mobiles
print(mobiles)