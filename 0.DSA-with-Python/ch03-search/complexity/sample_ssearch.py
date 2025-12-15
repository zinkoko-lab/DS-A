from typing import Any
from collections.abc import Sequence


def seq_search(a: Sequence, key: Any) -> int:
    i = 0  # 実行回数 = 1 -> 計算量 = O(1)
    n = len(a)  # 実行回数 = 1 -> 計算量 = O(1)

    while i < n:  # 実行回数 = n/2 -> 計算量 = O(n)
        if a[i] == key:  # 実行回数 = n/2 -> 計算量 = O(n)
            return i  # 実行回数 = 1 -> 計算量 = O(1)
        i += 1  # 実行回数 = n/2 -> 計算量 = O(n)

    return -1  # 実行回数 = 1 -> 計算量 = O(1)


"""
O(1) + O(1) + O(n) + O(n) + O(1) + O(n) + O(1)
= O(max(1, 1, n, n, 1, n, 1))
= O(n)
"""
