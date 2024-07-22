
n=5
for i in range(0,n):
    for j in range(0,n):
        if(i==0 or j==0 or i==n or j==n):
            print('*',end=' ')  
        else:
            print('',end=' ')      
    print() 