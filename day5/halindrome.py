'''def is_palindrome(s):
    return s == s[::-1]

def count_palindromes(strings):
    count = 0
    for string in strings:
        if is_palindrome(string):
            count += 1
        else:
            mid = len(string) // 2
            if is_palindrome(string[:mid]) or is_palindrome(string[mid:]):
                count += 1
    return count

# List of strings to check
s = ['aba', 'sasdda', 'aaaccc', 'taydog']
result = count_palindromes(s)
print("Count:" ,result)'''


s = ['aba', 'sasdda', 'aaaccc', 'tattdog']
count=0
for i in s:
    if i==i[::-1]:
        count+=1
    else:
        m=len(i)//2
        if len(i)%2==0:
            first=i[:m]
            second=i[m:]
            if first==first[::-1] or second==second[::-1]:
                count+=1
        else:
            first=i[:m+1]
            second=i[m+1:]
            if first==first[::-1] or second==second[::-1]:
                count+=1
print(count)
    



