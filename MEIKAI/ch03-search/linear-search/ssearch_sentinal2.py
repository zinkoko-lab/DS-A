from typing import Any
from collections.abc import Sequence
from copy import deepcopy


def seq_search(seq: Sequence, key: Any) -> int:
    """
    シーケンス a から key と等価な要素を線形探索(while文+番兵法)
    """
    a = deepcopy(seq)
    a.append(key)
    i = 0
    while a[i] != key:
        i += 1  # 余計にこの計算がされないように工夫
    return -1 if i == len(seq) else i


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
