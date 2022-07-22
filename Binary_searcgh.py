def binary_search(L,k):
    begin=0
    end=len(L)-1
    L.sort()
    while end-begin>=0:
        mid=(begin+end)//2
        if L[mid]>k:
            end=mid-1
        elif L[mid]<k:
            begin=mid+1
        else:
            return 1
    return 0    
    '''    
    if L[begin]==k or L[end]==k:
        return 1
    else:
        return 0
    '''
print(binary_search([2,56,22,890,3245],890) )   
            
