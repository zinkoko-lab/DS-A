print('1からnまでの整数の総和を求めます。')
n = int(input("nの値: "))
total = 0
i = 1
while i <= n:
    total += i
    i += 1

print(f"1から{n}までの総和は{total}です。")