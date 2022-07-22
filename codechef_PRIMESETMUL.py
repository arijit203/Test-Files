T=int(input())
st=input()
g=st.split()
count=1
flag=1
M=int(g[len(g)-1])
st=input()
g=st.split()
E=list(map(int,g))

for l in range(0,T):
    flag=1
    count=1
    for i in range(2,M):
        for j in range(2,i+1):
            
            
        
            if i%j==0:
                for k in range(2,j):
                    if j%k==0:
                        
                        flag=0
                        break
                if flag==1:
                    if j not in E:
                        break
                    else:
                        count+=1
                        
                    
                   
print(count)                    

