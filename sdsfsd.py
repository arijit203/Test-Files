import math
def bina(no,N):
    K=0
    count=N-1
    for i in no:
        print(i)
        K+=math.pow(2,count)*int(i)
        count-=1
    return int(K)
def prime(no):
    count=0
    for i in range(2,no):
        if no%i==0:
            return True
    return False        
        
def main(N,dip):
    for K in range(2,N+1):
        for j in range(0,N-K,K):
            
            if prime(bina(dip[i:i+K],N)) :
                return True
    return False        

T=int(input())
for i in range(T):
    N=int(input())
    dip=input()
    if main(N,dip) :
        print("Yes")
    else:
        print("No")
    
        
        
        
