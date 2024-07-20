# DICTIONARIES
# Dictionaies
menu={
    'chicken_biryani':555,
    'butter_chicken':450,
    'tandoori_chicken':400,
    'juicy_mandi':350
}
print(menu)

menu={
    'chicken_biryani':555,
    'butter_chicken':450,
    'tandoori_chicken':400,
    'juicy_mandi':350
}
menu['fruit_salad']=600 #for inserting the elements
print(menu)
print(menu.pop('chicken_biryani')) # for deleting the elements
print(menu)

print(menu.keys())
print(menu.values())

for k,v in menu.items():
    print(k,'->',v)

#count the fequency of each number 

arr=[1,3,6,2,5,3,7,5,1]
count=0
d={}
for key in arr:#i=key
    if key not in d:
        d[key]=1
    else:
        d[key]+=1
print(d)