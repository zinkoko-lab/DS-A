print("1からnまでの整数の数値の総和を求めます。")

n = int(input("nの値: "))
total = 0
for i in range(1, n+1):
    total += i

print(f'1から{n}までの数値の総和は{total}です。')