# n個の記号文字 * を w個ごとに改行しながら表示(その1)

n = int(input("全部で何個: "))
w = int(input("何個ごとに改行: "))

for i in range(1, n+1):
    print('*', end='')
    if i % w == 0: print()

if n % w:
    print()