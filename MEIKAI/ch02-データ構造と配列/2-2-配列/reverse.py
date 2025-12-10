from typing import Any
from collections.abc import MutableSequence


def reverse_array(a: MutableSequence) -> None:
    """
    ミュータブルなシーケンス a の要素の並びを反転
    """
    lenght = len(a)
    for i in range(lenght // 2):
        a[i], a[lenght - i - 1] = a[lenght - i - 1], a[i]


if __name__ == "__main__":
    print("配列の要素の並びを反転します。")
    nx = int(input("要素数は: "))
    x = [None] * nx
    for i in range(nx):
        x[i] = input(f"x[{i}] = ")

    reverse_array(x)

    print("配列の並びを反転しました。")
    for i, val in enumerate(x):
        print(f"x[{i}] = {val}")
