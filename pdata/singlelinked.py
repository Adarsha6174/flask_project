class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
        # print(data)
class LinkedList:
    def __init__(self): 
        self.head=None  #what is none
    def Start(self,data):
        new_node=Node(data)
        self.head=new_node
    def End(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        last_node=self.head
        while last_node.next:
            last_node=last_node.next
        last_node.next=new_node
    def Display(self):
        if self.head:
            node=self.head
            while node:
                print(node.data)
                node=node.next
        else:
            print("Linked List is empty")
ref=LinkedList()
ref.End(1)
# ref.End(2)
# ref.End(3)
# ref.End(4)
ref.Display()
        
    