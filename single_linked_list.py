from node import Node
class Singlelinklist:
    def __init__(self):
        self.head= None
    def is_empty(self):
        return self.head is None 
    def append(self,data):
        new_node=Node(data)

        if self.is_empty():
            self.head = new_node
            return
        current =self.head
        while current.next is not None:
            current=current.next
        current.next=new_node
    def insert(self,index,data):
        new_node - Node(data)
        if index ==0:
            new_node.next = self.head
            self.head = new_node
            return
        current= self.head
        postion =0
        while current is not None and position < index -1:
            current = current.next
            postion+= 1
        if current is None:
            print("index is out of order")
            return
    new_node.next = current.next
    current.next =new_node
    def pop(self):
        if self.is_empty():
            print("list is empty")
            return 
        if self.head.next is None:
            self.head = Nonereturn
        current + self.head
        while current.next.next is not None:
            current=current.next
        current.next= None

    def remove_at_index(self,index):
        if self.is_empty():
            print("list is empty")
            return
        if index == 0:
            self.head= self.head.next
            return
        current = self.head
        for i in range(index-1):
            if current is None or current.next is None:
                print("index out of oder")
                return
            current= current.next
        if current.next is None:
            print("out of order")
            return
        current.next = current.next.next

    def display(self):
        if self.is_empty():
            print("list is empty")
            return
        current=self.head
        while current is not None:
            print(current.data)
            current = current.next 
        return None
list = Singlelinklist()
list.append(10)
list.display()
list.pop()
