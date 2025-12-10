# 記号文字 + と　- を交互に表示（その１）

print("記号文字 + と - を交互に表示します。")
n = int(input("何個表示しますか？: "))

# 奇数 -> -
# 偶数 -> +

for i in range(n // 2):
    print('+-', end='')

if n % 2:
    print('+', end='')

print()
