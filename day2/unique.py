
#print unique elements

arr=[1,3,6,2,5,3,7,5,1]
count=0
d={}
for key in arr:#i=key
    if key not in d:
        d[key]=1
    else:
        d[key]+=1
for num,count in d.items():
    if count==1:#if count>1 it prints repeated numbers
        print(num)
