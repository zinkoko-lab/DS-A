# 1からnまでの整数の総和を求める(入力された数値を正の整数に制限をかける)

print("1からnまでの総和を求めます。")

while True:
    n = int(input("整数n: "))
    if n <= 0:
        print("整数nは 0 以上ある必要がある。もう一度入力してください！")
    else:
        break

total = 0

for i in range(1, n + 1):
    if i == n:
        print(f"{i} = ", end='')
    else:
        print(f"{i} + ", end='')
    total += i

print(total)