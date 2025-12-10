# 右下側が直角の二等辺三角形

print("右下側が直角の二等辺三角形")
n = int(input('短辺の長さ: '))

for i in range(n):
    for j in range(n):
        if j + 1 < n - i:
            print(' ', end='')
        else:
            print('*', end='')
    print()