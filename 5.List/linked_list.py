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
                print(current.val, end=' -> ')
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
        ptr = self.head
        while ptr.next:
            ptr = ptr.next
        ptr.next = new_node

    # def add(self, idex)


ll = LinkedList()
ll.addFirst('C')
ll.addFirst('A')
ll.addLast('D')
print(ll.countNode())