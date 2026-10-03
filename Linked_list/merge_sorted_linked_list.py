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


def merge_two_lists(list1, list2):

    current1 = list1.head
    current2 = list2.head

    dummy = Node(0)
    current = dummy

    while current1 and current2:

        if current1.data <= current2.data:
            current.next = current1
            current1 = current1.next

        else:
            current.next = current2
            current2 = current2.next

        current = current.next

    if current1:
        current.next = current1

    if current2:
        current.next = current2

    result = LinkedList()
    result.head = dummy.next

    return result


list1 = LinkedList()
list1.append(1)
list1.append(2)
list1.append(4)

list2 = LinkedList()
list2.append(1)
list2.append(3)
list2.append(4)

merged = merge_two_lists(list1, list2)

merged.print_list()