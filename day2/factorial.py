
#factorial using recursion

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
n=int(input())
print(fact(n))

#without recursion

n=int(input())
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)



#who wins cong .bjp

cong={7:5,18:22,32:8,71:5,66:6}#->values on left side is age right side votes
bjp={7:15,18:20,32:4,71:9,66:2}

cong_sum=0
bjp_sum=0
for age,votes in cong.items():
  if age>=18:
    cong_sum+=votes
for age,votes in bjp.items():
   if age>=18:
    bjp_sum+=votes
diff=abs(cong_sum-bjp_sum)#abs-absolute which is used to print the -ve numbers in +ve
if cong_sum>bjp_sum:
      print('cong win:',diff)
else:
      print('bjp win:',diff)

#recursion works based on base condition
#while using recursion dont use loops