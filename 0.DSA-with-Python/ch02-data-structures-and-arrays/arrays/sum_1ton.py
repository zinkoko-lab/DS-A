def sum_1ton(n: int) -> int:
    total = 0
    while n:
        total += n
        n -= 1
    return total


if __name__ == "__main__":
    print("1からxまでの総和を求めます。")
    x = int(input("整数x: "))
    print(f"1から{x}までの総和は {sum_1ton(x)} です。")
