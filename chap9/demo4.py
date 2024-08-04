# 字符串中的大小写转换的方法
s = 'hello, python'
a = s.upper()  # 转成大写之后，会产生一个新的字符串对象
print(a, id(a))
print(s, id(s))
b = s.lower()  # 转换之后，会产生一个新的字符串对象
print(b, id(b))
print(s, id(s))
print(b == s)
print(b is s)  # False

s2 = 'hello, Python'
print(s2.swapcase())

print(s2.title())
