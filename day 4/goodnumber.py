
#good number:
#arr=[35,9,1]  low=1 high=
#res=low cube + high cube
'''import math
print(math.ceil(10/4))->3'''

import math
arr=[35,9,1]
#res=lowcube+highcube
count=0
for i in arr:
    low=1
    high=(math.ceil(i**0.3))#->math.ceil(35**.3)
    while low<high:
        res=low**3+high**3
        if res==i:
            count+=1
        if res<i:
            low+=1
        else:     
          high-=1
print('the count:',count)  
