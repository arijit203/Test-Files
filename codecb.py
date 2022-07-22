n=int(input())
arr=[]
k=[]
for i in range(n):
    arr.append(int(input()))
print(arr)    
while len(arr)!=1:    
    k=arr.sort()
    print(k)
    x=k[0]
    y=k[1]
    arr.remove(x)
    arr.remove(y)
    arr.append((3*x+2*y)%100)
print(arr[0])    
