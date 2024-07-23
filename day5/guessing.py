#guessing number
'''import random
ran=random.randint(1,50)
print(ran)#->rand number 
chances=3
while chances>=1:
   guess=int(input('enter the number'))
   if guess==ran:
      print('congrats')
      break
   else:
      chances-=1
      continue
if chances<1:   
    print('failed try next time')'''



#for infinty checks
import random
ran=random.randint(1,12)
print(ran)#->rand number 
while True:
    guess=int(input('enter the number'))
    if guess==ran:
      print('congrats')
      break
    else:
      continue  
    print('failed try next time')     