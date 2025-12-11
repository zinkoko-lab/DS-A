# 記号文字 + と　- を交互に表示（その１）

print("記号文字 + と - を交互に表示します。")
n = int(input("何個表示しますか？: "))

# 奇数 -> -
# 偶数 -> +

for i in range(n):
    if i % 2: # 奇数
        print('-', end='')
    else:
        print('+', end='')

print()