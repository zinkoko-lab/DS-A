from max import max_of

print("配列の最大値を求めます。")
print('注："End"で入力終了。')

number = 0  # 空のリスト
x = []

while True:
    element = input(f"x[{number}] = ")
    if element == "End":
        break
    x.append(int(element))
    number += 1


print(x)
print(f"最大値は{max_of(x)}です。")
