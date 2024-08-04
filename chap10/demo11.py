def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# 斐波那契数列第 6 位上的数字
print(fib(6))

print('----------------------------------')
# 输出这个数列前 6 位上的数字
for i in range(1, 7):
    print(fib(i))
