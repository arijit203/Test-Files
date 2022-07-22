def sort(L):
    if L==[]:
        return L
    mini=min(L)
    L.remove(mini)
    return [mini]+sort(L)
print(sort([9,80,6,88,33,245,0,87]))
