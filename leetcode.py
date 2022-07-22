from math import sqrt
t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    l=[]
    l[::]=s
    print(l)
    if l.count("1")==n:
        v=int(s,2)
        print(type(v))
        flag=0
        copy=v
        if v>1:
            for i in range(2, int(sqrt(v) + 1)):
                if n%i == 0:
                    flag=1
                    break
        if flag==0:
            print("Yes")
        else:
            print("No")
    else:
        if s.find("10") != -1:
            print("Yes")
        else:
            print("No")
