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

    def remove_duplicates(self):
        current = self.head

        while current and current.next:

            if current.data == current.next.data:
                current.next = current.next.next

            else:
                current = current.next


linked = LinkedList()

linked.append(1)
linked.append(1)
linked.append(2)
linked.append(3)
linked.append(3)

print("Before:")
linked.print_list()

linked.remove_duplicates()

print("After:")
linked.print_list()