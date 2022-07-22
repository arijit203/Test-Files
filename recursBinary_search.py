import random
def Binary_search(L,k,begin,end):
    
    if end-begin>=0:
        mid=(begin+end)//2
        
        if k<L[mid]:
            end=mid-1
        elif k>L[mid]:
            begin=mid+1
        else:
            return 1
    else:
        return 0
    return Binary_search(L,k,begin,end)
L=[random.randrange(100) for i in range(10)]
L.sort()
print(L)
print(Binary_search(L,90,0,len(L)-1)  ) 
        
    
        
    
