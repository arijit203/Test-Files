Y=float(input("enter initial account balance"))
X=float(input("transaction amt"))
if X%5==0:
    Y=Y-X-0.5
    print("Balance:",Y)
else:
    print("Balance:",Y)
    
