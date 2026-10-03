class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None 
    def append(self, data):
        new_node = Node(data)
        if self.head is None:     
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        
        current.next = new_node
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next 
        print("None") 
    def merege(linked1,linked2):
        linked1=linked1.head
        linked2=linked2.head
        cur1=linked1.head
        cur2=linked2.head
        while cur1:
            cur1next=cur1.next
            cur2next=cur2.next
            if cur1.data<=cur2.data:
                cur1.next=cur2
                cur2=cur1next



        

        

linked1=LinkedList()
linked1.append(1)
linked1.append(2)
linked1.append(3)
linked1.append(4)
linked1.append(5)

linked2=LinkedList()
linked2.append(1)
linked2.append(2)
linked2.append(3)
linked2.append(4)
linked2.append(5)

linked2.print_list()
