#palindrome
'''s='malayalam'
s1=''
for i in range(len(s)-1,-1,-1):#
  s1+=s[i]
if(s1==s):
    print('palin')  
else :
    print('not palin') '''


#s=input()
#n=str(n)
# print(s[::-1])'''  
'''class solution:
    def isPalindrome(x):
        return (len(s)-1,-1,-1)
x=input()
print(isPalindrome(x))'''

#palindrome using functions

class Solution:
    def isPalindrome(self, x):
        s = str(x) 
        return s == s[::-1]
solution = Solution()   
x = input()
print(solution.isPalindrome(x))


#print sum of number until the it prints single digit

def sum_of_digits_until_single_digit(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

number = 23456
result = sum_of_digits_until_single_digit(number)
print(result) 