import math

for t in range (int(input())):
    n,x=map(int,input().split())
    arr=list(map(int,input().split()))
    
    d=[]
    for i in range (n):
        d.append([arr[i],(arr[i]/x),i])
    d.sort(key=lambda x: x[1])
    
    for i in d:
        print(i[2]+1,end=" ")
    
    print()    

            
        
