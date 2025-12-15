# 線形探索を行う関数seq_searchの利用例(その1)

from ssearch_while import seq_search

print("実数の探索を行います。")
print("注: 'End'で入力終了。")

number = 0
x = []

while True:
    s = input(f"x[{number}]: ")
    if s == "End":
        break
    x.append(float(s))
    number += 1

ky = float(input("探す値: "))

id = seq_search(x, ky)
if id == -1:
    print("その値の要素が存在しません。")
else:
    print(f"{ky} は x[{id}] にあります。")
