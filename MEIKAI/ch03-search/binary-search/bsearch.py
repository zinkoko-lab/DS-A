from typing import Any
from collections.abc import Sequence


def bin_search(a: Sequence, key: Any) -> int:
    pl = 0
    pr = len(a) - 1
    while pl <= pr:
        pc = (pl + pr) // 2
        if a[pc] == key:  # 終了条件-1 -> a[pc] == key -> 探索成功！
            return pc

        elif key > a[pc]:  # key > a[pc] -> 探索範囲を中央より右に絞る
            pl = pc + 1

        else:  # key < a[pc] -> 探索範囲を中央より左に絞る
            pr = pc - 1
    else:
        return -1  # 探索の対象範囲が無くなった！


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
