def bulla(n):
    flag=0
    for i in range(2,n):
        if n%i==0:
            flag=1
            break
    if flag==0:
        return True
    else:
        return False



T=int(input())
for i in range(T):
    p=int(input())
    
    l=input().split()
    l=list(map(int,l))
    ma=max((l))
    mi=min((l))
    count=0
    for i in range(mi,ma+1):
        b=bulla(i)
        if b:
            count+=1
    print(count)        
            
