#password verification
'''s=input()
ucount,lcount,dcount,scount=0,0,0,0
for c in s:
    if c.isupper:
        ucount+=1
    elif c.islower():
        lcount+=1
    elif c.isdigit():
        dcount+=1
    else:
        scount+=1
if len(s)>8 and ucount>0 and lcount>0 and dcount>0 and scount>0:
    print('valid')
else:
    print('invalid')'''

#hackrank 
#apple and oranges   sam shouse is 7{s} end 11{t}  two tress a is 3 and b is 13 find how many apples fall in sam house fallin right means count 1
#range of a is a+i<=t and a+i>=s
'''s=7
t=11
a=3
b=15
counta=0
countb=0
apples=[6,5,-4]
oranges=[9,8,-4]
for i in apples:
    if i+a in range(s,t+1):
      counta+=1
for i in oranges:
    if i+b in range(s,t+1):
      countb+=1
print(counta,countb) '''       
     