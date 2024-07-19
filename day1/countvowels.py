#count vowels in the string

#range is used if we know no.of iteration
s=input()
#s='Satwika'
vowels=['a','e','i','o','u','A','E','I','O','U']
count=0
for c in s:
   if c in vowels:
      count+=1
print(count)  