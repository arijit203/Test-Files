def pop(L,ma):
    a=[]
    for i in L:
        a.append(ma-i)
    return a
        
    
    
T=int(input())
for i in range(T):
    N,K=map(int,input().split())
    L=list(map(int,input().split()))
    while K>0:
        ma=max(L)
        L=pop(L,ma)
    for i in range(N):
        print(L[i],end=' ')
        
