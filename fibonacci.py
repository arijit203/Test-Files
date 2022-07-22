"""
def fib(n):
    a=0
    b=1
    for i in range(0,n):
        a,b=b,a+b
    return a
n=int(input())
for i in range(n):
    print(fib(i))

"""
def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-2)+fib(n-1)
n=int(input())
for i in range(n):
    print(fib(i))
