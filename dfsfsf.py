n=int(input())
count=1
L=["Manoj","Ravi","Harish","Seema","Abinav"]
while count<n:
    k=L.pop(0)
    L.append(k)
    L.append(k)
    count+=1
print(L[0])    
    
