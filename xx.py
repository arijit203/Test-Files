
T=int(input())
for i in range(T):
    p=int(input())
    
    l=input().split()
    l=list(map(int,l))
    print(l)
    ma=max((l))
    mi=min((l))
    print(ma,mi)
    count=0
    for i in range(mi,ma+1):
        b=prime(i)
        if b:
            count+=1
    print(count)        
  

def prime(n):
    flag=0
    for i in range(2,n):
        if n%i==0:
            flag=1
            break
    if flag==0:
        return True
    else:
        return False

            
