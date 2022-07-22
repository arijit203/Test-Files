def dfs(k,n,x,dist,graph):
    if k==n:
        x+=[dist[n]]
        return
    else:
        for i in range(1,n+1):
            if dist[i]==-1 and graph[k][i]!=0:
                dist[i]=dist[k]+graph[k][i]
                dfs(i,n,x,dist,graph)
                dist[i]=-1
T=int(input())
for i in range(T):
    graph=[[0 for i in range(11)]for j in range(11)]
    print(graph)
    v,e=map(int,input().split())
    for j in range(v):
        x,y,w=map(int,input().split())
        graph[x][y]=w
        graph[y][x]=w
    x=[]
    dist=[-1]*(v+1)
    print(dist)
    dist[1]=0
    print(dist)
    dfs(1,v,x,dist,graph)
    x.sort()
    val=x[0]
    ans=0
    for i in range(0,len(x)):
        if val==x[i]:
            ans+=1
    print(ans)        
    
