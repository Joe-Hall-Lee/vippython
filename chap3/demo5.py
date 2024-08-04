# 比较运算符,比较运算符的结果为 bool 类型
a, b = 10, 20
print('a > b 吗？', a > b)  # False
print('a < b 吗？', a < b)  # True
print('a <= b 吗？', a <= b)  # True
print('a >= b 吗？', a >= b)  # False
print('a == b 吗？', a == b)  # False
print('a != b 吗？', a != b)  # True
'''
= 称为赋值运算符，== 称为比较运算符。
一个变量由三部分组成，标识、类型、值。
== 比较的是值还是标识呢？ 比较的是值。
比较对象的标识使用的是 is。
'''
a = 10
b = 10
print(a == b)  # True 说明 a 与 b 的 value 相等
print(a is b)  # True 说明 a 与 b 的 id 相等
# 以下代码没学过，后面会给大家讲解
lst1 = [11, 22, 33, 44]
lst2 = [11, 22, 33, 44]
print(lst1 == lst2)  # value --> True
print(lst1 is lst2)  # id --> False
print(id(lst1))
print(id(lst2))
print(a is not b)  # False，a 的 id 与 b 的 id 不是不相等的
print(lst1 is not b)  # True
