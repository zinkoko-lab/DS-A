def sqSum(num):
    sum = num**2
    if (num-1):
        sum += sqSum(num - 1)
    return sum

print(sqSum(100))

'''
sqSum(100)
sum = 100**2
(100-1)== 99 => true
sum = 100**2 + sqSum(99)

sqSum(99)
sum = 99**2
(99-1)== 98 => true
sum = 99**2 + sqSum(98)

sqSum(98)
sum = 98**2
(98-1) == 97 => true
sum = 98**2 + sqSum(97)

...

sqSum(2)
sum = 2**2
(2-1) == 1 => true
sum = 2**2 + sqSum(1)

sqSum(1)
sum = 1**1
(1-1) == 0 => false
return sum
'''