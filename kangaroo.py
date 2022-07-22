
def kangaroo(x1, v1, x2, v2):
    
    if x1<x2 and v1<v2:
        return "NO"
    else:
        i=1
        con=x2-x1
        g,h=0,0
        while True:
            
            if (i*v1)==(i*v2)+con:
                return "YES"
            g=v1*i
            h=v2*i+con
            if h<g and v2<v1:
                print(i)
                
                return "NO"
            
            i+=1    
        return "NO"
print(kangaroo(0,3,4,2)  )  
