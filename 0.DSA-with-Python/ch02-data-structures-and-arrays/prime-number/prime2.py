# 1,000以下の素数を列挙します。

print("1,000以下の素数を列挙します。")

# 処理

counter = 0  # 除算回数をカウントします
prime = [2]

for n in range(3, 1001, 2):
    for i in range(1, len(prime)):
        counter += 1
        if n % prime[i] == 0:
            break
    else:
        prime.append(n)

print(prime)
print(f"除算回数は{counter}")
