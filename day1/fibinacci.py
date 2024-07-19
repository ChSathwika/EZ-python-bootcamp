
#fibinocci series 
def check(n):
    first=0
    second=1
    print(first,second,end=' ')
    count=2
    while count<=n:
        third=first+second
        print(third,end=' ')
        first=second
        second=third
        count+=1#if we wont use then infinfity loop 
check(10)
