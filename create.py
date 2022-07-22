import string
G=[1,2,3]
k=90
def create():
    l=string.ascii_lowercase
    l=list(l)
    print(k)
    d={}
    for i in range(len(l)):
        d[l[i]]=l[(i+3)%26]
        
create()
