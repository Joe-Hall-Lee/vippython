print('apple' > 'app')  # True
print('apple' > 'banana')  # False
print(ord('a'), ord('b'))
print(ord('周'))

print(chr(97), chr(98))
print(chr(21608))

'''
    == 与 is 的区别
    == 比较的是 value
    is 比较的是 id 是否相等
'''
a = b = 'Python'
c = 'Python'
print(a == b)  # True
print(b == c)  # True
print(a is b)  # True
print(b is c)  # True
print(id(a))  # 1286702454448
print(id(b))  # 1286702454448
print(id(c))  # 1286702454448
