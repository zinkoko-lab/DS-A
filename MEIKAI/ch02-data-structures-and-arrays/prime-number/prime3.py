# 1,000以下の素数を列挙します。

print("1,000以下の素数を列挙します。")

# 処理

counter = 0  # 除算回数をカウントします
prime = [2, 3]

for n in range(5, 1001, 2):
    i = 1
    while prime[i] * prime[i] <= n:
        counter += 2
        if n % prime[i] == 0:
            break
        i += 1
    else:
        prime.append(n)
        counter += 1

print(prime)
print(f"乗除算回数は{counter}")
