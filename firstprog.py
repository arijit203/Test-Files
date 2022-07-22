no=int(input())
count=0
for i in range(2,int(no/2)):
    if no%i==0:
        count+=1
    
if count==0:
    print("prime")
else:
    print("Not prime")
