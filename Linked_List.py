class Node():
    def __init__(self,data=None,nex=None):
        self.data=data
        self.next=nex
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_at_beginning(self,data):
        node=Node(data,self.head)
        self.head=node
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr=self.head
        llstr=""
        while itr:
            llstr+=str(itr.data)+"---->"
            itr=itr.next
        print(llstr)
if __name__=="__main":
    ll=linkedlist()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(89)
    ll.print()
