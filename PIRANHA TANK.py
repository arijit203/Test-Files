def bulla(n):
    count=0
    for i in range(1,n):
        if n%i==0:
            count+=1
    if count==1:
        return True
    else :
        return False



def case(T):
    
    for i in range(T):
        p=int(input())
        l=input().split()
        l=list(map(int,l))
        ma=max((l))
        mi=min((l))
        return(k(mi,ma))
def k(mi,ma):
    count=0
    for i in range(mi,ma+1):
        b=bulla(i)
        if b:
            count+=1
    return(count)
if __name__ == '__main__':
    T=int(input())
    print(case(T))
          
