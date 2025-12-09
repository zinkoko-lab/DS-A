from linked_list import LinkedList


class Stack(LinkedList):

    def push(self, val):
        return super().add_last(val)

    def pop(self):
        return super().remove_last()

    def get_val(self):
        return super().print_list()

    def peek(self):
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        return cur_node.val


if __name__ == "__main__":

    # PUSH 1 -> PUSH 5 -> POP -> PUSH 7 -> PUSH 6 -> PUSH 4 -> POP -> POP -> PUSH 3
    # final result ---> 1->7->3
    stack = Stack()
    stack.push(1)  # PUSH 1
    stack.push(5)  # PUSH 5
    print(stack.pop())  # POP
    stack.push(7)  # PUSH 7
    stack.push(6)  # PUSH 6
    stack.push(4)  # PUSH 4
    print(stack.pop())
    print(stack.pop())
    stack.push(3)  # PUSH 3
    stack.get_val()
    print(stack.peek())
