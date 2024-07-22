
#s='1c0c1c1a0b1'   a=& b=| c=^
s='1a1b1c0c1b0a1'
res=int(s[0])
for i in range(1,len(s),2):
 if s[i]=='a':
  res=res&int(s[i+1])
 elif s[i]=='b':
  res=res|int(s[i+1])
 elif s[i]=='c':
   res=res^int(s[i+1])
print(res) 