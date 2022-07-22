def white(st,N):
    K=N-len(st)
    if K!=0:
        while K>0:
            
            
                
T=int(input())
for i in range(T):
    L=input().split()
    k=[]
    p=[]
    s=''
    N,w=int(L[0]),int(L[1])
    for j in range(0,N):
        k.append(input())
    
    for j in ((k)):
        
        if len(s)+len(j)<=w:
            s=s+j+" "
            
        else:
            p.append(s.rstrip())
            s=''
            s=j+' '
            
    p.append(s.rstrip())    
    for j in p:
        print(white(j,w))
    
