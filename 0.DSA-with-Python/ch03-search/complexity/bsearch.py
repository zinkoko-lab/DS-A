from typing import Any
from collections.abc import Sequence


def bin_search(a: Sequence, key: Any) -> int:
    pl = 0  # 実行回数 = 1 -> 計算量 = O(1)
    pr = len(a) - 1  # 実行回数 = 1 -> 計算量 = O(1)
    while pl <= pr:  # 実行回数 = log n -> 計算量 = O(log n)
        pc = (pl + pr) // 2  # 実行回数 = log n -> 計算量 = O(log n)
        if a[pc] == key:  # 実行回数 = log n -> 計算量 = O(log n)
            return pc  # 実行回数 = 1 -> 計算量 = O(1)

        elif key > a[pc]:  # 実行回数 = log n -> 計算量 = O(log n)
            pl = pc + 1  # 実行回数 = log n -> 計算量 = O(log n)

        else:
            pr = pc - 1  # 実行回数 = log n -> 計算量 = O(log n)
    else:
        return -1  # 実行回数 = 1 -> 計算量 = O(1)


"""
O(1) + O(1) + O(log n) + O(log n) + O(log n) + O(log n) + O(log n) + O(log n) + O(1)
= O(max(1, 1, log n, log n, log n, log n, log n, log n, 1))
= O(log n)
"""


if __name__ == "__main__":
    n = int(input("要素数: "))
    x = []
    print("昇順に入力してください。")
    for i in range(n):
        x.append(int(input(f"x[{i}]: ")))

    ky = int(input("探す値: "))
    id = bin_search(x, ky)
    if id == -1:
        print("その値の要素は存在しません。")
    else:
        print(f"{ky} は x[{id}] にあります。")
