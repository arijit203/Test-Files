def unique(L):
    L_uniq = [ ]
    for i in range(0, len(L)):
        if not(L[i] in L[i + 1: ]):
            L_uniq.append(L[i])
    return L_uniq
print(unique([1,2,1,3,4,5,4]))
