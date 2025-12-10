# n個の記号文字 * を w個ごとに改行しながら表示(その2)

n = int(input("全部で何個: "))
w = int(input("何個ごとに改行: "))

'''
for _ in range(n // w):
    print('*' * w)

print('*' * (n % w))
'''

print((n//w)*(('*'*w)+'\n') + '*'*(n%w))