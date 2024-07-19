

# given a string a1b2c3 print digits sum

'''s=input()
sum=0
for i in range(0,len(s)):
    if s[i].isdigit():
        sum=sum+int(s[i]) #here we use int(s[i]) becoz string cannot be added so we have to typecast a string into integer
print(sum)'''

#count the digits
s=input()
count=0
for i in range(0,len(s)):
    if s[i].isdigit():
        count+=1
print(count)