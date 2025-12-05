class Node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def printList(self):
        current = self.head
        while current:
            if current.next:
                print(current.val, end=" -> ")
            else:
                print(current.val)
            current = current.next

    def countNode(self):
        cnt = 0
        current = self.head
        while current:
            cnt += 1
            current = current.next
        return cnt

    def addFirst(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def addLast(self, val):
        new_node = Node(val)
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def add(self, index, val):
        if self.countNode():
            if index > 0 and index <= (self.countNode() + 1):
                new_node = Node(val)
                current_index = 1
                current = self.head
                while current_index < (index - 1):
                    current = current.next
                    current_index += 1
                if current.next:
                    new_node.next = current.next
                    current.next = new_node
                else:
                    current.next = new_node
            elif index > 0 and index > (self.countNode() + 1):
                raise IndexError("index out of range")
            else:
                self.addLast(val)
        else:
            if index == 1 or index == -1:
                self.addFirst(val)
            else:
                raise IndexError("index out of range")


ll = LinkedList()
ll.addFirst("C")
ll.addFirst("B")
ll.addFirst("A")
ll.addLast("E")
print(ll.countNode())
ll.printList()
ll.add(-1, "F")
ll.printList()
