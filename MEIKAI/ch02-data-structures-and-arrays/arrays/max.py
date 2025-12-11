from typing import Any
from collections.abc import Sequence


def max_of(a: Sequence) -> Any:
    """
    シーケンス a の要素の最大値を返却する\n
    Return the maximum member element of 'sequence a'.
    """
    if not a:
        raise ValueError("empty sequence")

    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]

    return maximum


if __name__ == "__main__":
    print("配列の最大値を求めます。")
    num = int(input("要素数: "))
    x = [None] * num

    for i in range(num):
        x[i] = input(f"x[{i}] = ")

    print(f"最大値は{max_of(x)}です。")
