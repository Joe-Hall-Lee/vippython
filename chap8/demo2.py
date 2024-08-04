'''元组的创建方式'''
'''第一种，使用()'''

t = ('Python', 10, 89)
print(t)
print(type(t))

t2 = 'Python', 10, 89  # 省略了小括号
print(t2)
print(type(t2))
t3 = ('Python',)  # 如果元组中只有一个元素，逗号不能省
print(t3)
print(type(t3))
'''第二种创建方式，使用内置函数 tuple()'''
t1 = tuple(('Python', 10, 89))
print(t1)
print(type(t1))

'''空元组的创建方式'''
'''空列表的创建方式'''
lst = []
lst1 = list()
d = {}
d2 = dict()

# 空元组
t4 = ()
t5 = tuple()

print('空列表', lst, lst1)
print('空字典', d, d2)
print('空元组', t4, t5)
