import random

def max3(a,b,c):

    maximum = a
    if b > maximum: maximum = b
    if c > maximum: maximum = c

    return maximum

def generate_random_int():
    return random.randint(1,3)

for _ in range(30):
    a = generate_random_int()
    b = generate_random_int()
    c = generate_random_int()
    print(f"max3({a}, {b}, {c}) = {max3(a, b, c)}")