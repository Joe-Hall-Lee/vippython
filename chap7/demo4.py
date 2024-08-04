scores = {'张三': 1, '李四': 2, '王五': 3}
# 获取所有的 key
keys = scores.keys()
print(keys)
print(type(keys))
print(list(keys))  # 将所有的 key 组成的视图转成列表

# 获取所有的 value
values = scores.values()
print(values)
print(type(values))
print(list(values))

# 获取所有的 key-value 对
items = scores.items()
print(items)
print(list(items))  # 转换之后的列表元素由元组组成
