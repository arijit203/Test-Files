def square(n):
    sum=0
    for i in range(n):
        sum+=n
    return sum   
T=int(input())
for i in range(T):
    no=(input())
    L=[]
    for i in no:
        L.append(str(square(int(i))))
    print(''.join(L))
        
