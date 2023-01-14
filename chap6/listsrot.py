lst = [10, 20, 30, 50, 40]
print('排序前的列表', lst, id(lst))
# 开始排序，调用列表对象的sort方法，升序排序
lst.sort()
print('排序后的列表', lst, id(lst))

# 通过指定关键字参数，将列表中的元素进行降序排序
lst.sort(reverse=True)
print(lst)
lst.sort(reverse=False)
print(lst)
print('------使用内置函数sorted（）对列表进行排序，将产生一个新的列表对象---------------')
lst = [10, 20, 30, 50, 40]
print('原列表', lst)
# 开始排序
new_lst = sorted(lst)
print(lst)
print(new_lst)
# 指定关键字参数，实现列表元素的降序排序
desc_lst = sorted(lst, reverse=True)
print(desc_lst)
