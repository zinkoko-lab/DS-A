from src import linked_list
import pytest
import string
import random

CHARS = list(string.ascii_letters + string.digits)


# =============================================
# testing Node object
def test_Node():
    for _ in range(1000):
        val2 = random.choice(CHARS)
        node2 = linked_list.Node(val2)
        val1 = random.choice(CHARS)
        node1 = linked_list.Node(val1, node2)
        assert node2.val == val2
        assert node2.next == None
        assert node1.val == val1
        assert node1.next == node2


# =============================================

# testing LinkList object


# =============================================
# LinkList Constructor
def test_init():
    # initial linked list has the head 'None'
    sample_list = linked_list.LinkedList()
    assert sample_list.head == None


# =============================================
# LinkList add_first


# 空っぽのリストの先頭に新しいnodeを追加する
def test_add_first_1():
    sample_list = linked_list.LinkedList()
    first_node_val = random.choice(CHARS)
    sample_list.add_first(first_node_val)
    assert sample_list.head.val == first_node_val
    assert sample_list.head.next == None


# 空っぽでないリストの先頭に新しいnodeを追加する
# A -> B -> C -> D
def test_add_first_2():
    sample_list = linked_list.LinkedList()
    for _ in range(1000):
        first_val = random.choice(CHARS)
        sample_list.add_first(first_val)
        first_node = sample_list.head
        assert first_val == first_node.val


# =============================================
# LinkList add_last


# 空っぽのリストの末尾に新しいnodeを追加するとlistの先頭に追加となること
# add_last method の内の add_firstの実行の確認
def test_add_last_1():
    for _ in range(1000):
        sample_list = linked_list.LinkedList()
        last_val = random.choice(CHARS)
        sample_list.add_last(last_val)
        assert last_val == sample_list.head.val


# 空っぽでないリストの末尾に新しいnodeを追加できること
def test_add_last_2():
    sample_list = linked_list.LinkedList()
    for i in range(1000):
        val = random.choice(CHARS)
        sample_list.add_last(val)

    for i in range(1000):
        last_val = sample_list.count_node() + i + 1
        sample_list.add_last(last_val)
        cur_node = sample_list.head
        while cur_node.next:
            cur_node = cur_node.next
        assert last_val == cur_node.val


# =============================================
# LinkList add
# 与えられた index が有効であるかどうか check する機能の挙動


# 空っぽのlistに範囲外のindex番号にnodeを追加不可
def test_add_1():
    for i in range(1000):
        empty_list = linked_list.LinkedList()
        with pytest.raises(IndexError) as e:
            empty_list.add(empty_list.count_node() + 2 + i, random.choice(CHARS))
        assert str(e.value) == "index out of range"


# 空っぽでないlistに範囲外のindex番号にnodeを追加不可
def test_add_2():
    sample_list = linked_list.LinkedList()
    for i in range(100):
        val = random.choice(CHARS)
        sample_list.add_last(val)

    for i in range(1000):
        index = sample_list.count_node() + 2 + i
        with pytest.raises(IndexError) as e:
            sample_list.add(index, random.choice(CHARS))
        assert str(e.value) == "index out of range"


# 空っぽでないlistのindex番号0にnodeを追加不可
def test_add_3():
    sample_list = linked_list.LinkedList()
    for _ in range(1000):
        val = random.choice(CHARS)
        sample_list.add_last(val)
        with pytest.raises(IndexError) as e:
            sample_list.add(0, random.choice(CHARS))
        assert str(e.value) == "invalid index number"


# 空っぽのlistのindex番号0にnodeを追加不可
def test_add_4():
    sample_list = linked_list.LinkedList()
    with pytest.raises(IndexError) as e:
        sample_list.add(0, random.choice(CHARS))
    assert str(e.value) == "invalid index number"


# 空っぽのlistのindex番号1にnodeを追加可
def test_add_5():
    for _ in range(1000):
        sample_list = linked_list.LinkedList()
        val = random.choice(CHARS)
        sample_list.add(1, val)
        assert sample_list.head.val == val
        assert sample_list.head.next == None


# 空っぽでないlistのindex番号1にnodeを追加可
def test_add_6():
    sample_list = linked_list.LinkedList()
    sample_list.add_first(random.choice(CHARS))
    for _ in range(1000):
        val = random.choice(CHARS)
        sample_list.add(1, val)
        first_node = sample_list.head
        assert val == first_node.val


# 空っぽでないlist
# index==list-size+1
# 末尾にnodeが入ること
def test_add_7():
    sample_list = linked_list.LinkedList()
    sample_list.add_first(random.choice(CHARS))
    for _ in range(1000):
        size = sample_list.count_node()
        val = random.choice(CHARS)
        sample_list.add(size + 1, val)
        cur_node = sample_list.head
        while cur_node.next:
            cur_node = cur_node.next
        assert val == cur_node.val


# 空っぽでないlist
# index < 0
# 末尾にnodeが入ること
def test_add_8():
    sample_list = linked_list.LinkedList()
    for _ in range(1000):
        sample_list.add_last(random.choice(CHARS))
        size = sample_list.count_node()
        idx = random.randint(1, 1000 * size) * (-1)
        val = random.choice(CHARS)
        sample_list.add(idx, val)
        cur_node = sample_list.head
        while cur_node.next:
            cur_node = cur_node.next
        assert val == cur_node.val


# 空っぽでないlist
# 1 < index <= size
def test_add_9():
    sample_list = linked_list.LinkedList()
    for _ in range(1000):
        sample_list.add_last(random.choice(CHARS))
    for _ in range(1000):
        size = sample_list.count_node()
        idx = random.randint(2, size)
        val = random.choice(CHARS)
        sample_list.add(idx, val)
        cur_idx = 1
        cur_node = sample_list.head
        while cur_idx < idx:
            cur_node = cur_node.next
            cur_idx += 1
        target_node = cur_node.next
        assert idx == cur_idx
        assert val == cur_node.val


# =============================================
# LinkList remove_first


# 空っぽのlist -> エラーを表示
def test_remove_first_1():
    for _ in range(100):
        sample_list = linked_list.LinkedList()
        with pytest.raises(IndexError) as e:
            sample_list.remove_first()
        assert str(e.value) == "This is an empty linked list and no element to remove."


# 空っぽでないときlistの先頭にnodeを削除可
def test_remove_first_2():
    for _ in range(1000):
        sample_list = linked_list.LinkedList()
        for j in range(100):
            sample_list.add_last(random.choice(CHARS))
        assert sample_list.head.val == sample_list.remove_first()


# 空っぽでないとき
# node 1 個だけある
# listの先頭にnodeを削除可
def test_remove_first_3():
    for _ in range(1000):
        sample_list = linked_list.LinkedList()
        val = random.choice(CHARS)
        sample_list.add_first(val)
        assert sample_list.head.val == sample_list.remove_first()
        assert sample_list.head == None


# =============================================
# LinkList remove_last


# 空っぽのlist -> エラーを表示
def test_remove_last_1():
    for _ in range(100):
        sample_list = linked_list.LinkedList()
        with pytest.raises(IndexError) as e:
            sample_list.remove_last()
        assert str(e.value) == "This is an empty linked list and no element to remove."


# 空っぽでないとき
# node 1 個だけある
# listの先頭にnodeを削除することになる
def test_remove_last_2():
    for _ in range(1000):
        sample_list = linked_list.LinkedList()
        val = random.choice(CHARS)
        sample_list.add_first(val)
        assert sample_list.head.val == sample_list.remove_last()
        assert sample_list.head == None


# 空っぽでないときlistの末尾のnodeを削除可
def test_remove_last_3():
    sample_list = linked_list.LinkedList()
    for _ in range(1000):
        val = random.choice(CHARS)
        sample_list.add_last(val)
        cur_node = sample_list.head
        while cur_node.next:
            cur_node = cur_node.next
        assert val == sample_list.remove_last()
        assert cur_node.next == None


# =============================================
# LinkList remove


# listが空っぽのときは、エラーを表示する
def test_remove_1():
    sample_list = linked_list.LinkedList()
    for _ in range(1000):
        idx = random.randint(1, 1000)
        with pytest.raises(IndexError) as e:
            sample_list.remove(idx)
        assert str(e.value) == "This is an empty linked list and no element to remove."


# 指定index番号が範囲外のとき
# -------------------------


# index > size
def test_remove_2():
    sample_list = linked_list.LinkedList()
    for i in range(1000):
        sample_list.add_last(random.choice(CHARS))
        size = sample_list.count_node()
        idx = random.randint(size + 1, 100 * size)
        with pytest.raises(IndexError) as e:
            sample_list.remove(idx)
        assert str(e.value) == "index out of range"


# index == 0
def test_remove_3():
    sample_list = linked_list.LinkedList()
    for _ in range(100):
        sample_list.add_last(random.choice(CHARS))

    for _ in range(1000):
        with pytest.raises(IndexError) as e:
            sample_list.remove(0)
        assert str(e.value) == "invalid index number"


# index == 1 -> remove_first が実行される
def test_remove_4():
    sample_list = linked_list.LinkedList()
    for _ in range(1000):
        sample_list.add_first(random.choice(CHARS))
    for _ in range(1000):
        val = random.choice(CHARS)
        sample_list.add_first(val)
        head_after_remove_first = sample_list.head.next
        assert val == sample_list.remove(1)
        assert head_after_remove_first == sample_list.head


# index < 0 -> remove_last が実行される
def test_remove_5():
    sample_list = linked_list.LinkedList()
    for _ in range(1000):
        sample_list.add_last(random.choice(CHARS))

    size = sample_list.count_node()

    while size:
        cur_node = sample_list.head
        while cur_node.next:
            cur_node = cur_node.next
        target = cur_node
        idx = random.randint(1, 100 * size) * (-1)
        assert target.val == sample_list.remove(idx)
        assert target.next == None
        size = sample_list.count_node()


# index == size -> remove_last が実行される
def test_remove_6():
    sample_list = linked_list.LinkedList()
    for _ in range(1000):
        sample_list.add_last(random.choice(CHARS))

    size = sample_list.count_node()

    while size:
        cur_node = sample_list.head
        while cur_node.next:
            cur_node = cur_node.next
        target = cur_node
        assert target.val == sample_list.remove(size)
        assert target.next == None
        size = sample_list.count_node()


# 1 < index < size の場合:
def test_remove_7():
    sample_list = linked_list.LinkedList()
    for _ in range(1000):
        sample_list.add_last(random.choice(CHARS))

    size = sample_list.count_node()
    while size >= 3:
        idx = random.randint(2, size - 1)
        cur_node = sample_list.head
        cur_idx = 1
        while cur_idx < idx:
            cur_node = cur_node.next
            cur_idx += 1
        target = cur_node
        assert target.val == sample_list.remove(idx)
        assert size - 1 == sample_list.count_node()
        size = sample_list.count_node()


# =============================================
# LinkList count_node
def test_count_node():
    sample_list = linked_list.LinkedList()
    for i in range(1000):
        sample_list.add_last(random.choice(CHARS))
        assert i + 1 == sample_list.count_node()


# =============================================
# LinkList print_list
def test_print_list(capsys):
    for n in range(1000):
        result_str = ""
        sample_list = linked_list.LinkedList()
        num_nodes = n + 1
        for i in range(num_nodes):
            val = random.choice(CHARS)
            result_str += val + "\n" if i == num_nodes - 1 else val + " -> "
            sample_list.add_last(val)

        sample_list.print_list()
        captured = capsys.readouterr()
        assert captured.out == result_str


# =============================================
