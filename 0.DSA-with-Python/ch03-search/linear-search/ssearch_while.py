from typing import Any
from collections.abc import Sequence


def seq_search(a: Sequence, key: Any) -> int:
    """
    シーケンス a から key と等価な要素を線形探索(while文)
    """
    i = 0
    while True:
        if i == len(a):
            return -1
        if a[i] == key:
            return i
        i += 1


if __name__ == "__main__":

    num = int(input("配列の要素数: "))
    array = [None] * num

    for i in range(num):
        array[i] = int(input(f"array[{i}]: "))

    ky = int(input("探す値: "))

    idx = seq_search(array, ky)

    if idx == -1:
        print("その値の要素が存在しません。")
    else:
        print(f"{ky}は array[{idx}]にあります。")
