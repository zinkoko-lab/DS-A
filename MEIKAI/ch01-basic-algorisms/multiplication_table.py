# 九九表を表示

print('_'*27)
for i in range(1, 10):
    for j in range(1, 10):
        print(f'{i * j :3}', end='')
    print()
print('_'*27)