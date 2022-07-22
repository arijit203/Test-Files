T=int(input())
count=False
for k in range(T):
    s=input()
    count=False
    for i in range(1,len(s)-1):
        if s[i]=="0":
            if s[i-1]=="1" and s[i+1]=="1":
                count=True
                print("$$")
                break
        else:
            if s[i-1]=="0" and s[i+1]=="0":
                count=True
                break
    if count=="True":
        print("Good")
    else:
        print("Bad")
