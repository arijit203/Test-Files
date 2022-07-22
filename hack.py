n=int(input())
d={}
L=list(map(int,input().split()))
count=1
for i in range(len(L)):
    d[i]=0
while len(L)!=0:
    for i in range(0,len(L)):
        d[i]=count
        L[i]-=1
        count+=1
    if L[i]==0:
        L.remove(0)
for i in d:
    print(d[i],end=" ")
            
        
