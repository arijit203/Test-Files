n=int(input())
R=1
C=1
k=1
while R<=(2*n-1):
    C=1
    while C<=n:
        
        if C<=k:
            print(C,end='')
            if C!=R:
                print(",",end='')
        C+=1        
    R+=1    
    print() 
    if R>n:
        k-=1
    else:
        k+=1
            
            
            
