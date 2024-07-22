#s=a1b2c3d492nm45 output=1234924abcdnm
s='a1b2c3d492nm45'
s1=''
s2=''
for c in s:
  if c.isdigit():
    s1+=c
  else:
    s2+=c
print(s1+s2)    