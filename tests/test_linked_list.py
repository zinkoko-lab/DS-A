from src import linked_list
import pytest


# testing Node object
def test_Node():
    node2 = linked_list.Node("List!")
    node1 = linked_list.Node("Hello", node2)
    assert node2.val == "List!"
    assert node2.next == None
    assert node1.val == "Hello"
    assert node1.next == node2


def test_linked_list(capsys):
    # initial linked list has the head 'None'
    sample_list = linked_list.LinkedList()
    assert sample_list.head == None

    # test add_first
    # 空っぽのリストの先頭に新しいnodeを追加する
    sample_list.add_first("C")
    assert sample_list.head.val == "C"
    assert sample_list.head.next == None

    # 空っぽでないリストの先頭に新しいnodeを追加する
    sample_list.add_first("B")
    assert sample_list.head.val == "B"
    assert sample_list.head.next.val == "C"
    assert sample_list.head.next.next == None

    # test add_last

    # add_last patern-1
    # 空っぽのリストの末尾に新しいnodeを追加すると追加できること
    single_node_list = linked_list.LinkedList()
    single_node_list.add_last("A")
    assert single_node_list.head.val == "A"
    assert single_node_list.head.next == None

    # add_last patern-2
    # 空っぽでないリストの末尾に新しいnodeを追加する
    sample_list.add_last("D")
    first = sample_list.head
    second = first.next
    last = second.next
    assert last.val == "D"

    # test count_node
    length = sample_list.count_node()
    assert length == 3

    # test print_list
    # listが空っぽでない場合
    sample_list.print_list()
    captured = capsys.readouterr()
    assert captured.out == "B -> C -> D\n"
    # listが空っぽである場合
    empty_list = linked_list.LinkedList()
    empty_list.print_list()
    captured = capsys.readouterr()
    assert captured.out == "This is an empty linked-list.\n"

    # test error IndexError("index out of range") of _validat_index(indirectly)
    with pytest.raises(IndexError) as e:
        sample_list.add(7, "E")
    assert str(e.value) == "index out of range"

    # test error IndexError("index out of range") of _validat_index(indirectly) & listが空っぽのとき
    with pytest.raises(IndexError) as e:
        empty_list.add(3, "E")
    assert str(e.value) == "index out of range"

    # test error IndexError("invalid index number") of _validat_index(indirectly)
    with pytest.raises(IndexError) as e:
        sample_list.add(0, "N")
    assert str(e.value) == "invalid index number"

    # test add
    # add の中の add_firstの挙動の確認
    sample_list.add(1, "A")
    sample_list.print_list()
    captured = capsys.readouterr()
    assert captured.out == "A -> B -> C -> D\n"

    # add の中の add_lastの挙動の確認
    sample_list.add(5, "E")
    sample_list.print_list()
    captured = capsys.readouterr()
    assert captured.out == "A -> B -> C -> D -> E\n"

    # 任意のindexの位置に node を追加できる
    sample_list.add(3, "S")
    sample_list.print_list()
    captured = capsys.readouterr()
    assert captured.out == "A -> B -> S -> C -> D -> E\n"

    # test remove first

    # 空っぽのlistから先頭のnodeを削除しようとするとエラーとなる
    empty_list = linked_list.LinkedList()
    with pytest.raises(IndexError) as e:
        empty_list.remove_first()
    assert str(e.value) == "This is an empty linked list and no element to remove."

    # 空っぽでないlistから先頭のnodeを削除する
    sample_list.remove_first()
    sample_list.print_list()
    captured = capsys.readouterr()
    assert captured.out == "B -> S -> C -> D -> E\n"

    # test remove last
    # 空っぽのlistから先頭のnodeを削除しようとするとエラーとなる
    with pytest.raises(IndexError) as e:
        empty_list.remove_last()
    assert str(e.value) == "This is an empty linked list and no element to remove."

    # 空っぽでないlistから末尾のnodeを削除する
    sample_list.remove_last()
    sample_list.print_list()
    captured = capsys.readouterr()
    assert captured.out == "B -> S -> C -> D\n"

    # test remove
    # 空っぽのlistから任意のindexのnodeを削除しようとするとエラーとなる
    with pytest.raises(IndexError) as e:
        empty_list.remove(3)
    assert str(e.value) == "This is an empty linked list and no element to remove."

    # 任意の index の node を削除できる
    sample_list.remove(2)
    sample_list.print_list()
    captured = capsys.readouterr()
    assert captured.out == "B -> C -> D\n"

    # remove の中の remove_first の挙動
    sample_list.remove(1)
    sample_list.print_list()
    captured = capsys.readouterr()
    assert captured.out == "C -> D\n"

    # remove の中の remove_last の挙動
    sample_list.remove(2)
    sample_list.print_list()
    captured = capsys.readouterr()
    assert captured.out == "C\n"
