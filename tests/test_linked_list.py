from src import linked_list
import pytest


# =============================================
# testing Node object
def test_Node():
    node2 = linked_list.Node("List!")
    node1 = linked_list.Node("Hello", node2)
    assert node2.val == "List!"
    assert node2.next == None
    assert node1.val == "Hello"
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
    sample_list.add_first("A")
    assert sample_list.head.val == "A"
    assert sample_list.head.next == None


# 空っぽでないリストの先頭に新しいnodeを追加する
# A -> B -> C -> D
def test_add_first_2(capsys):
    test_vals = ["D", "C", "B", "A"]
    sample_list = linked_list.LinkedList()
    for val in test_vals:
        sample_list.add_first(val)

    sample_list.print_list()
    captured = capsys.readouterr()
    assert captured.out == "A -> B -> C -> D\n"


# =============================================
# LinkList add_last


# 空っぽのリストの末尾に新しいnodeを追加するとlistの先頭に追加となること
# add_last method の内の add_firstの実行の確認
def test_add_last_1():
    sample_list = linked_list.LinkedList()
    sample_list.add_last("A")
    assert sample_list.head.val == "A"


# 空っぽでないリストの末尾に新しいnodeを追加できること
def test_add_last_2(capsys):
    test_vals = ["A", "B", "C", "D"]
    sample_list = linked_list.LinkedList()
    for val in test_vals:
        sample_list.add_last(val)

    sample_list.print_list()
    captured = capsys.readouterr()
    assert captured.out == "A -> B -> C -> D\n"


# =============================================
# LinkList add
# 与えられた index が有効であるかどうか check する機能の挙動


# 空っぽのlistに範囲外のindex番号にnodeを追加不可
def test_add_1():
    empty_list = linked_list.LinkedList()
    with pytest.raises(IndexError) as e:
        empty_list.add(5, "A")
    assert str(e.value) == "index out of range"


# 空っぽでないlistに範囲外のindex番号にnodeを追加不可
def test_add_2():
    test_vals = ["A", "B", "C", "D"]
    sample_list = linked_list.LinkedList()
    for val in test_vals:
        sample_list.add_last(val)

    for i in range(100):
        index = len(test_vals) + 2 + i
        with pytest.raises(IndexError) as e:
            sample_list.add(index, "R")
        assert str(e.value) == "index out of range"


# 空っぽでないlistのindex番号0にnodeを追加不可
def test_add_3():
    test_vals = ["A", "B", "C", "D"]
    sample_list = linked_list.LinkedList()
    for val in test_vals:
        sample_list.add_last(val)

    with pytest.raises(IndexError) as e:
        sample_list.add(0, "" "Z")
    assert str(e.value) == "invalid index number"


# 空っぽのlistのindex番号0にnodeを追加不可
def test_add_4():
    sample_list = linked_list.LinkedList()
    with pytest.raises(IndexError) as e:
        sample_list.add(0, "Z")
    assert str(e.value) == "invalid index number"


# 空っぽのlistのindex番号1にnodeを追加可
def test_add_5():
    sample_list = linked_list.LinkedList()
    sample_list.add(1, "A")
    assert sample_list.head.val == "A"
    assert sample_list.head.next == None


# 空っぽでないlistのindex番号1にnodeを追加可
def test_add_6():
    test_vals = ["A", "B", "C", "D"]
    sample_list = linked_list.LinkedList()
    for val in test_vals:
        sample_list.add_last(val)

    sample_list.add(1, "head")
    assert sample_list.head.val == "head"
    assert sample_list.head.next.val == "A"


# 空っぽでないlist
# index==list-size+1
# 末尾にnodeが入ること
def test_add_7(capsys):
    test_vals = ["A", "B", "C", "D"]
    sample_list = linked_list.LinkedList()
    for val in test_vals:
        sample_list.add_last(val)

    last_index = len(test_vals) + 1
    sample_list.add(last_index, "tail")
    sample_list.print_list()
    captured = capsys.readouterr()
    assert captured.out == "A -> B -> C -> D -> tail\n"


# 空っぽでないlist
# index < 0
# 末尾にnodeが入ること
def test_add_8(capsys):
    test_vals = ["A", "B", "C", "D"]
    sample_list = linked_list.LinkedList()
    for val in test_vals:
        sample_list.add_last(val)

    minus_index = -3
    sample_list.add(minus_index, "negative")
    sample_list.print_list()
    captured = capsys.readouterr()
    assert captured.out == "A -> B -> C -> D -> negative\n"


# 空っぽでないlist
# 1 < index <= size
def test_add_9(capsys):
    test_vals = ["A", "B", "C", "D"]
    sample_list = linked_list.LinkedList()
    for val in test_vals:
        sample_list.add_last(val)

    middle_index = 3
    sample_list.add(middle_index, "middle")
    sample_list.print_list()
    captured = capsys.readouterr()
    assert captured.out == "A -> B -> middle -> C -> D\n"


# =============================================
# LinkList remove_first


# 空っぽのlist -> エラーを表示
def test_remove_first_1():
    sample_list = linked_list.LinkedList()
    with pytest.raises(IndexError) as e:
        sample_list.remove_first()
    assert str(e.value) == "This is an empty linked list and no element to remove."


# 空っぽでないときlistの先頭にnodeを削除可
def test_remove_first_2(capsys):
    test_vals = ["A", "B", "C", "D"]
    sample_list = linked_list.LinkedList()
    for val in test_vals:
        sample_list.add_last(val)

    sample_list.remove_first()
    sample_list.print_list()
    captured = capsys.readouterr()
    assert captured.out == "B -> C -> D\n"


# 空っぽでないとき
# node 1 個だけある
# listの先頭にnodeを削除可
def test_remove_first_3():
    sample_list = linked_list.LinkedList()
    sample_list.add_last("A")
    sample_list.remove_first()
    assert sample_list.head == None


# =============================================
# LinkList remove_last


# 空っぽのlist -> エラーを表示
def test_remove_last_1():
    sample_list = linked_list.LinkedList()
    with pytest.raises(IndexError) as e:
        sample_list.remove_last()
    assert str(e.value) == "This is an empty linked list and no element to remove."


# 空っぽでないとき
# node 1 個だけある
# listの先頭にnodeを削除することになる
def test_remove_last_2():
    sample_list = linked_list.LinkedList()
    sample_list.add_last("A")
    sample_list.remove_last()
    assert sample_list.head == None


# 空っぽでないときlistの末尾のnodeを削除可
def test_remove_last_3(capsys):
    test_vals = ["A", "B", "C", "D"]
    sample_list = linked_list.LinkedList()
    for val in test_vals:
        sample_list.add_last(val)

    sample_list.remove_last()
    sample_list.print_list()
    captured = capsys.readouterr()
    assert captured.out == "A -> B -> C\n"


# =============================================
# LinkList remove


# listが空っぽのときは、エラーを表示する
def test_remove_1():
    sample_list = linked_list.LinkedList()
    for i in range(100):
        with pytest.raises(IndexError) as e:
            sample_list.remove(i + 1)
        assert str(e.value) == "This is an empty linked list and no element to remove."


# 指定index番号が範囲外のとき
# -------------------------


# index > size
def test_remove_2():
    test_vals = ["A", "B", "C", "D"]
    sample_list = linked_list.LinkedList()
    for val in test_vals:
        sample_list.add_last(val)

    size = len(test_vals)
    for i in range(100):
        idx = size + 1 + i
        with pytest.raises(IndexError) as e:
            sample_list.remove(idx)
        assert str(e.value) == "index out of range"


# index == 0
def test_remove_3():
    test_vals = ["A", "B", "C", "D"]
    sample_list = linked_list.LinkedList()
    for val in test_vals:
        sample_list.add_last(val)

    with pytest.raises(IndexError) as e:
        sample_list.remove(0)
    assert str(e.value) == "invalid index number"


# index == 1 -> remove_first が実行される
def test_remove_4(capsys):
    test_vals = ["A", "B", "C", "D"]
    sample_list = linked_list.LinkedList()
    for val in test_vals:
        sample_list.add_last(val)

    sample_list.remove(1)
    sample_list.print_list()
    captured = capsys.readouterr()
    assert captured.out == "B -> C -> D\n"


# index < 0 -> remove_last が実行される
def test_remove_5(capsys):
    test_vals = ["A", "B", "C", "D"]
    sample_list = linked_list.LinkedList()
    for val in test_vals:
        sample_list.add_last(val)

    sample_list.remove(-3)
    sample_list.print_list()
    captured = capsys.readouterr()
    assert captured.out == "A -> B -> C\n"


# index == size -> remove_last が実行される
def test_remove_5(capsys):
    test_vals = ["A", "B", "C", "D"]
    sample_list = linked_list.LinkedList()
    for val in test_vals:
        sample_list.add_last(val)

    index = len(test_vals)
    sample_list.remove(index)
    sample_list.print_list()
    captured = capsys.readouterr()
    assert captured.out == "A -> B -> C\n"


# index < 0 -> remove_last が実行される
def test_remove_6(capsys):
    test_vals = ["A", "B", "C", "D"]
    sample_list = linked_list.LinkedList()
    for val in test_vals:
        sample_list.add_last(val)

    sample_list.remove(-3)
    sample_list.print_list()
    captured = capsys.readouterr()
    assert captured.out == "A -> B -> C\n"


# 1 < index <= size の場合:
def test_remove_7(capsys):
    test_vals = ["A", "B", "middle", "C", "D"]
    sample_list = linked_list.LinkedList()
    for val in test_vals:
        sample_list.add_last(val)

    sample_list.remove(3)
    sample_list.print_list()
    captured = capsys.readouterr()
    assert captured.out == "A -> B -> C -> D\n"


# =============================================
# LinkList count_node
def test_count_node(capsys):
    num_nodes = 100
    sample_list = linked_list.LinkedList()
    for val in range(num_nodes):
        sample_list.add_last(val)

    assert num_nodes == sample_list.count_node()


# =============================================
# LinkList print_list
def test_print_list(capsys):
    num_nodes = 100
    result_str = ""
    sample_list = linked_list.LinkedList()
    for i in range(num_nodes):
        val = i + 1
        result_str += str(val) + " -> " if val < num_nodes else str(val) + "\n"
        sample_list.add_last(val)

    sample_list.print_list()
    captured = capsys.readouterr()
    assert captured.out == result_str


# =============================================
