from __future__ import annotations
from typing import Any
import hashlib


class Bucket:

    def __init__(self, key: Any, val: Any, next: Bucket | None = None) -> None:
        """initialize Bucket"""
        self.key = key
        self.val = val
        self.next = next


class ChainedHash:

    def __init__(self, capacity: int) -> None:
        """初期化"""
        self.capacity = capacity
        self.table = [None] * self.capacity

    def hash_value(self, key: Any) -> int:
        """初期化"""
        if isinstance(key, int):
            return key % self.capacity
        else:
            return (
                int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity
            )

    def search(self, key: Any) -> int:
        """キー'key'を持つ要素を探索し、その要素が持つ値を返却"""
        hash = self.hash_value(key)
        p = self.table[hash]

        if p is not None:
            if p.key == key:
                return p.val
            p = p.next

        return None

    def add(self, key: Any, value: Any | None = None) -> bool:
        """キーが key で 値が value の要素を追加する"""
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None:
            if p.key == key:
                return False  # 追加失敗
            p = p.next

        new_bucket = Bucket(key, value, self.table[hash])
        self.table[hash] = new_bucket
        return True  # 追加成功

    def remove(self, key: Any) -> bool:
        """キー key を持つ要素を削除"""
        hash = self.hash_value(key)
        p = self.table[hash]

        # table[hash] が空っぽのとき
        if p is None:
            print("A")
            print(f"There is no bucket with the key of {key}.")
            return False  # 削除失敗

        # 先頭の bucket にkeyを持っている要素があるとき
        if p.key == key:
            print(f"{key}が table{[hash]}の 先頭にありました")
            self.table[hash] = p.next
            if p.next is not None:  # 先頭に bucketが一個だけあるかどうか確認する
                p.next = None
            return True

        # 末尾の bucket にkeyを持っているとき
        # 先頭と末尾の間の bucket にkeyを持っているとき

        while p.next is not None:
            if p.next.key == key:
                target_bucket = p.next  # keyを持つ bucket までたどり着く
                break
            p = p.next
        else:
            print("C")
            print(f"There is no bucket with the key of {key}.")
            return False  # 同じkeyを持つ bucket が無かった。

        # 末尾に key を持つ bucket があるとき
        if target_bucket.next is None:
            p.next = None
            print(f"{key}が table{[hash]}の 末尾にありました")
            return True
        else:
            p.next = target_bucket.next
            target_bucket.next = None
            print(f"{key}が table{[hash]}の 中間の位置にありました")
            return True

    def dump(self) -> None:
        for i in range(self.capacity):
            p = self.table[i]
            print(f"{i:02}", end="")
            while p is not None:
                print(f" -> {p.key} ({p.val if p.val is not None else ''})", end="")
                p = p.next
            print()


if __name__ == "__main__":

    ch_hash = ChainedHash(13)
    ch_hash.add(14)
    ch_hash.add(29)
    ch_hash.add(17)
    ch_hash.add(69)
    ch_hash.add(5)
    ch_hash.add(6)
    ch_hash.add(33)
    ch_hash.add(20)
    ch_hash.add(46)
    ch_hash.add(13)

    # key = 33の値を探索
    print(f"key = {33} の要素の値は '{ch_hash.search(33)}' です。")

    if not ch_hash.add(33, "something"):
        print("key が衝突しました。")

    # ch_hash.remove(20)

    ch_hash.dump()
