# a から b までの総和を求める（求める式も表示：その２）
a = int(input("整数a: "))
b = int(input("整数b: "))

if a > b:
    a, b = b, a

total = 0
for i in range(a, b):
    print(f"{i} + ", end='')
    total += i

print(f"{b} = ", end='')
total += b
print(total)

