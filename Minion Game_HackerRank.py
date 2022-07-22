def minion_game(string):
    # your code goes here
    s1=0
    s2=0         
    string=string.upper()
    st=[string[i:j] for i in range(len(string))
      for j in range(i+1,len(string)+1)]
    
    for word in st:
        if vowel_matcher(word[0]):
            s2+=1
        else:
            s1+=1
            
    if s2 > s1:
        print("Kevin",s2)
    elif s1 > s2:
        print("Stuart",s1)
    else:
        print("Draw")    

def vowel_matcher(ch):
    if ch in ["A","E","I","O","U"]:
        return 1
    else:
        return 0
if __name__ == '__main__':
    s = input()
    minion_game(s)
