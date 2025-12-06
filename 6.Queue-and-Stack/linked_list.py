class Node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def count_node(self):
        count = 0
        cur = self.head
        while cur:
            cur = cur.next
            count += 1
        return count

    def print_list(self):
        if not self.head:
            print("This is an empty linked-list.")
            return

        cur = self.head
        while cur:
            print(cur.val, end=" -> " if cur.next else "\n")
            cur = cur.next

    #  listの任意の index の node を削除/追加するメソッドを実行する際に
    # 与えられた index が有効であるかどうか check するプラベートメソッド
    def _validate_index(self, index, size):
        # (listの長さ+1)より大きいindex番号を与ると、範囲外エラーとなる
        if index > size + 1:
            raise IndexError("index out of range")

        # index-1 start 仕様だと考え、index番号を0と与えたときはエラーとなる
        if index == 0:
            raise IndexError("invalid index number")

    # listの先頭に new node を加えるメソッド
    def add_first(self, val):
        new = Node(val)
        new.next = self.head
        self.head = new

    # 末尾に new node を加えるメソッド
    def add_last(self, val):
        # 空っぽの list であれば、先頭に new node を加える
        if not self.head:
            self.add_first(val)
            return

        # 空っぽでないときは、先頭から一個一個たどって最後の nodeに辿り着くまで行く
        new = Node(val)
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new

    # listの任意のindex に new node を加えるメソッド
    def add(self, index, val):

        size = self.count_node()
        self._validate_index(
            index, size
        )  # 与えられた index が有効であるかどうか check する

        # 有効な範囲は (1 ~ size + 1) or (index < 0)となる

        # index 番号が 1 の場合は listの先頭に new nodeを加える
        if index == 1:
            self.add_first(val)

        # index 番号がマイナスまたは size + 1の場合は末尾に new nodeを加える
        elif index < 0 or index == size + 1:
            self.add_last(val)

        # その他の場合(つまり 1 < index <= size)
        else:
            new = Node(val)
            cur = self.head
            cur_idx = 1
            while cur_idx < index - 1:
                cur = cur.next
                cur_idx += 1
            new.next = cur.next
            cur.next = new

    # listの先頭の node を削除するメソッド
    def remove_first(self):
        # listが空っぽのときはエラーを表示
        if not self.head:
            raise IndexError("This is an empty linked list and no element to remove.")
            return None

        cur = self.head
        self.head = cur.next
        cur.next = None
        return cur.val

    # listの最後の node を削除するメソッド
    def remove_last(self):
        # listが空っぽのときはエラ or listの中身は node 1個のみの場合は先頭を削除 => remove_first()へ
        if not self.head or self.count_node() == 1:
            self.remove_first()

        else:
            size = self.count_node()
            cur = self.head
            count = 1
            while count < size - 1:
                cur = cur.next
                count += 1
            target = cur.next
            cur.next = None
            return target.val

    #  listの任意の index の node を削除するメソッド
    def remove(self, index):

        size = self.count_node()
        self._validate_index(
            index, size
        )  # 与えられた index が有効であるかどうか check する

        # index の有効範囲は (1 ~ size + 1) or (index < 0)

        # index == 1の場合は、 先頭の nodeを削除するメソッドを実行
        if index == 1:
            self.remove_first()

        # index < 0 or index == size + 1 の場合は、最後の nodeを削除するメソッドを実行
        elif index == size and index < 0:
            self.remove_last()

        # 1 < index <= size の場合:
        else:
            cur = self.head
            count = 1
            while count < index - 1:
                cur = cur.next
                count += 1
            target = cur.next
            cur.next = target.next
            target.next = None


if __name__ == "__main__":
    some_quote = LinkedList()
    some_quote.add_first("if")
    some_quote.add_last("there")
    some_quote.add(3, "is")
    some_quote.add(4, "no")
    some_quote.add(5, "struggle")
    some_quote.add(6, "there")
    some_quote.add(7, "is")
    some_quote.add(8, "no")
    some_quote.add(9, "progress")
    some_quote.print_list()
    some_quote.remove(5)
    some_quote.add(5, "apple")
    some_quote.print_list()
