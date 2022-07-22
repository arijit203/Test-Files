T=int(input())
for i in range(T):
    N,A=map(int,input().split())
    L1=list(map(int,input().split()))
    L=[]
    d={}
    for i in range(N):
        L.append(i+1)
        d[i+1]=L1[i]
       
    
    for i in (L):
            
        if d[i]<=A:
            print(L,"    ",d)
            d[i]=0
            print(L.pop(0),end=" ")
        else:
            d[i]=d[i]-A
            k=L.pop(0)
            L.append(k)
                #print(L,"    ",d)
                
    print()                
            

