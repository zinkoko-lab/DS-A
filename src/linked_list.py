class Node:
    """
    A node in a singly linked list.

    Attributes:
        val: Any
            The value stored in the node.
        next: Node | None
            Reference to the next node in the list.
    """

    def __init__(self, val, next=None):
        """
        Initialize a new node.

        Args:
            val: any type
                The data the node should store.
            next: Node | None, optional
                Reference to the next node in the list. Defaults to None.
        """
        self.val = val
        self.next = next


class LinkedList:
    """
    A singly linked list implementation that supports indexed insertion and removal.
    Supports negative indexing for add/remove, treating negative index as 'append/remove last'.
    """

    def __init__(self, head=None):
        """
        Initialize an empty linked list.

        Args:
            head: Node | None, optional
                The initial head of the list. Defaults to None.
        """
        self.head = head

    def count_node(self):
        """
        Count the number of nodes in the linked list.

        Returns:
            int: The number of nodes.
        """
        count = 0
        cur = self.head
        while cur:
            cur = cur.next
            count += 1
        return count

    def print_list(self):
        """
        Print all values in the list from head to tail.
        Prints message if the list is empty.
        """
        if not self.head:
            print("This is an empty linked-list.")
            return

        cur = self.head
        while cur:
            print(cur.val, end=" -> " if cur.next else "\n")
            cur = cur.next

    def _validate_index(self, index, size, method):
        """
        Validate index for add/remove operations.

        Args:
            index (int): The index provided by user.
            size (int): Current size of the list.
            method (callable): The method that triggered validation (add/remove).

        Raises:
            IndexError: If index is out of valid range.
        """
        if index > size + 1 and method == self.add:
            raise IndexError("index out of range")
        if index > size and method == self.remove:
            raise IndexError("index out of range")
        if index == 0:
            raise IndexError("invalid index number")

    def add_first(self, val):
        """
        Insert a new node at the beginning of the list.

        Args:
            val: The value to insert.
        """
        new = Node(val)
        new.next = self.head
        self.head = new

    def add_last(self, val):
        """
        Insert a new node at the end of the list.

        Args:
            val: The value to insert.
        """
        if not self.head:
            return self.add_first(val)

        new = Node(val)
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new

    def add(self, index, val):
        """
        Insert a value at a specific index in the list.

        Supported index rules:
            - index == 1 → insert at head
            - index == size + 1 → append to end
            - index < 0 → treated as append to end
            - 1 < index <= size → insert in middle

        Args:
            index (int): Target position to insert.
            val: Value to insert.

        Raises:
            IndexError: If index is invalid.
        """
        size = self.count_node()
        self._validate_index(index, size, self.add)

        if index == 1:
            return self.add_first(val)
        elif index < 0 or index == size + 1:
            return self.add_last(val)

        new = Node(val)
        cur = self.head
        cur_idx = 1
        while cur_idx < index - 1:
            cur = cur.next
            cur_idx += 1

        new.next = cur.next
        cur.next = new

    def remove_first(self):
        """
        Remove and return the first node of the list.

        Returns:
            any: The value of the removed node.

        Raises:
            IndexError: If the list is empty.
        """
        if not self.head:
            raise IndexError("This is an empty linked list and no element to remove.")

        cur = self.head
        self.head = cur.next
        cur.next = None
        return cur.val

    def remove_last(self):
        """
        Remove and return the last node of the list.

        Returns:
            any: The value of the removed node.

        Raises:
            IndexError: If the list is empty.
        """
        size = self.count_node()

        if not self.head or size == 1:
            return self.remove_first()

        cur = self.head
        count = 1
        while count < size - 1:
            cur = cur.next
            count += 1

        target = cur.next
        cur.next = None
        return target.val

    def remove(self, index):
        """
        Remove and return the node at a specific index.

        Supported index rules:
            - index == 1 → remove first node
            - index == size → remove last node
            - index < 0 → remove last node
            - 1 < index < size → remove middle node

        Args:
            index (int): Position to remove.

        Returns:
            any: Value of the removed node.

        Raises:
            IndexError: If index is invalid or list is empty.
        """
        if not self.head:
            raise IndexError("This is an empty linked list and no element to remove.")

        size = self.count_node()
        self._validate_index(index, size, self.remove)

        if index == 1:
            return self.remove_first()
        elif index == size or index < 0:
            return self.remove_last()

        cur = self.head
        count = 1
        while count < index - 1:
            cur = cur.next
            count += 1

        target = cur.next
        cur.next = target.next
        target.next = None
        return target.val
