# リストの全要素を走査（インデックス値を使わない）

x = ['John', 'George', 'Paul', 'Ringo']

# for i in x:
#     print(iter(x))

it = iter(x)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# print(next(it))

