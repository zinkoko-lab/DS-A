class Node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def countNode(self):
        count = 0
        cur = self.head
        while cur:
            cur = cur.next
            count += 1
        return count

    def printList(self):
        if not self.head:
            print("This is an empty linked-list.")
            return

        cur = self.head
        while cur:
            print(cur.val, end=" -> " if cur.next else "\n")
            cur = cur.next

    def addFirst(self, val):
        new = Node(val)
        new.next = self.head
        self.head = new

    def addLast(self, val):
        if not self.head:
            self.addFirst(val)
            return

        new = Node(val)
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new

    def add(self, index, val):

        size = self.countNode()

        # index > size+1 => out of range
        if index > size + 1:
            raise IndexError("index out of range")
            return

        # index == 0 => invalid index
        if index == 0:
            raise IndexError("invalid index number")
            return

        #  index < 0, 0 < index < size+1 => ok
        # index == 1 => addFirst(index)
        if index == 1:
            self.addFirst(val)

        # index < 0 or index == size + 1 => addLast(index)
        elif index < 0 or index == size + 1:
            self.addLast(val)

        # 1 < index <= size + 1
        else:
            new = Node(val)
            cur = self.head
            cur_idx = 1
            while cur_idx < index - 1:
                cur = cur.next
                cur_idx += 1
            new.next = cur.next
            cur.next = new

    def removeFirst(self):
        if not self.head:
            raise IndexError("This is an empty linked list and no element to remove.")
            return

        cur = self.head
        self.head = cur.next
        cur.next = None

    def removeLast(self):
        if not self.head:
            raise IndexError("This is an empty linked list and no element to remove.")
            return

        if self.countNode() == 1:
            self.removeFirst()

        else:
            cur = self.head
            count = 1
            while count < self.countNode() - 1:
                cur = cur.next
                count += 1
            cur.next = None

    def remove(self, index):

        size = self.countNode()

        # index > size+1 => out of range
        if index > size + 1:
            raise IndexError("index out of range")
            return

        # index == 0 => invalid index
        if index == 0:
            raise IndexError("invalid index number")
            return

        # index == 1 => removeFirst
        if index == 1:
            self.removeFirst()

        # index == size or index < 0
        elif index == size and index < 0:
            self.removeLast()

        # 1 < index < size
        else:
            cur = self.head
            count = 1
            while count < index - 1:
                cur = cur.next
                count += 1
            target = cur.next
            cur.next = target.next
            target.next = None


some_quote = LinkedList()
some_quote.addFirst("if")
some_quote.addLast("there")
some_quote.add(3, "is")
some_quote.add(4, "no")
some_quote.add(5, "struggle")
some_quote.add(6, "there")
some_quote.add(7, "is")
some_quote.add(8, "no")
some_quote.add(9, "progress")
some_quote.printList()
some_quote.remove(5)
some_quote.add(5, "apple")
some_quote.printList()
