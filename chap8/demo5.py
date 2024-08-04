# 集合的创建方式
'''第一种创建方式，使用 {}'''
s = {1, 2, 3, 55, 55, 7}  # 集合中的元素不允许重复
print(s)

'''第二种创建方式'''

s1 = set(range(6))
print(s, type(s1))

s2 = set([1, 1, 3, 2, 4])
print(s2, type(s2))

s3 = set((1, 23, 3, 2, 44, 4, 4))  # 集合中的元素是无序的
print(s3, type(s3))

s4 = set('Python')
print(s4, type(s4))

s5 = set({1, 2, 3, 4, 66, 66, 7})
print(s5, type(s5))

# 定义一个空集合
s6 = {}  # dict 字典类型
print(type(s6))

s7 = set()
print(type(s7))
