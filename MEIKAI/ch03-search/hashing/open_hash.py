from __future__ import annotations
from typing import Any
from enum import Enum
import hashlib


# バケットの属性（データ格納, 空, 削除済み）
class Status(Enum):
    OCCUPIED = 0
    EMPTY = 1
    DELETED = 2


# バケットのclassの定義
class Bucket:

    def __init__(
        self, key: Any = None, value: Any = None, stat: Status = Status.EMPTY
    ) -> None:
        """初期化"""
        self.key = key  # キー
        self.value = value  # 値
        self.stat = stat  # 属性

    def set(self, key: Any, value: Any, stat: Status) -> None:
        """前フィールドに値を設定"""
        self.key = key
        self.value = value
        self.stat = stat

    def set_stat(self, stat: Status) -> None:
        """属性を設定"""
        self.stat = stat


# OpenHashのclassの定義
class OpenHash:

    def __init__(self, capacity: int) -> None:
        """初期化"""
        self.capacity = capacity  # hash table の容量
        self.table = [Bucket()] * self.capacity  # 空っぽの hash table を作成

    def hash_value(self, key: Any) -> int:
        """hash value を計算する"""
        if isinstance(key, int):
            return key % self.capacity
        else:
            int(hashlib.sha256(str(key)).hexdigest, 16) % self.capacity

    def rehash_value(self, key: Any) -> int:
        """hash value を再度計算する"""
        return (self.hash_value(key) + 1) % self.capacity

    def search_node(self, key: Any) -> Bucket:
        """キーがkeyを持つ bucketを探索"""
        hash = self.hash_value(key)
        p = self.table[hash]

        for i in range(self.capacity):
            if p.stat == Status.EMPTY:
                return None
            elif p.stat == Status.OCCUPIED and p.key == key:
                return p

            hash = self.rehash_value(key)
            p = self.table[hash]
        else:
            return None

    def search(self, key: Any) -> Any:
        """キーが key をもつ要素を探索(値を返却)"""
        p = self.search_node(key)
        if p != None:
            return p.value
        else:
            return None

    def add(self, key: Any, value: Any) -> bool:
        """キーがkeyで値がvalueを持つ要素を追加"""
        if self.search(key) != None:
            return False  # その keyの要素が登録済み

        hash = self.hash_value(key)
        p = self.table[hash]
        for i in range(self.capacity):
            if p.stat == Status.EMPTY or p.stat == Status.DELETED:
                self.table[hash] = Bucket(key, value, Status.OCCUPIED)
                return True  # 追加成功
            hash = self.rehash_value(key)
            p = self.table[hash]
        else:
            return False  # 追加失敗

    def remove(self, key: Any) -> bool:
        p = self.search_node(key)
        if p == None:
            return False
        p.set_stat(Status.DELETED)
        return True

    def dump(self) -> None:
        """hash table を表示"""
        for i in range(self.capacity):
            print(f"{i:2}", end="")
            if self.table[i].stat == Status.OCCUPIED:
                print(f"{self.table[i].key} {self.table[i].value}")
            elif self.table[i].stat == Status.EMPTY:
                print("-- 未登録 --")
            elif self.table[i].stat == Status.DELETED:
                print("-- 削除済み --")
