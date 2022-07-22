'''
import time
print(time.time())
a=time.time();print(sum(list(range(1000n))));b=time.time()
print(b-a)

def sum(n):
    if n<=0:
        return n
    else:
        return n+sum(n-1)
print(sum(100000))    

def reverse(L):

    if len(L)==0:
        return L
    else:
        return L[len(L)-1]+reverse(L[:len(L)-1])
print(reverse([1,2,3,4]))
def collatz(n):

    if n%2==0:
        k=n/2
        if n/2==1:
            return 1
    else:
        k=3n+1
         
    return 1+collatz(k)
print(collatz(7))'''
def equality(P, Q):
	return P == Q
print(equality([1,2,3],[1,2,3,4,5]))    
