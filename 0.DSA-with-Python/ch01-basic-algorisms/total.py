# aからbまでの総和を求める(for文)
# ２値ソートの２値変換

print("aからbまでの総和を求めます。")
a = int(input('整数a: '))
b = int(input('整数b: '))

if a > b:
    a, b = b, a

total = 0

for i in range(a, b+1):
    total += i

print(f"{a}から{b}までの総和は{total}です。")
