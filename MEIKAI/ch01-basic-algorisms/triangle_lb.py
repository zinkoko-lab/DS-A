# 左下側が直角の二等辺三角形

print("左下側が直角の二等辺三角形")
n = int(input('短辺の長さ: '))

for i in range(n):
    for j in range(n):
        if i == j: print('*'*(j+1))

