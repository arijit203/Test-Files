def subsets(nums):
    output=[[]]
    for no in nums:
        output+=[i+[no] for i in output]
    return output    
for i in range(int(input())):
    print()
    no=int(input())
    k=[b for b in range(1,no+1)]
    G=subsets(k)
    for i in G:
        for j in i:
            print(j,end=" ")
        print()    
        
