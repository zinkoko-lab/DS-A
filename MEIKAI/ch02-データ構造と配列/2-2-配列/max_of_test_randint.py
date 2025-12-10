from max import max_of
import random

print("乱数の最大値を求めます。")
no = int(input("乱数の個数: "))
lo = int(input("乱数の下限: "))
hi = int(input("乱数の上限: "))

x = [None] * no
for i in range(no):
    x[i] = random.randint(lo, hi)

print(x)
print(f"最大値は{max_of(x)}です。")
