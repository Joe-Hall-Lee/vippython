'''key 的判断'''
scores = {'张三': 1, '李四': 2, '王五': 3}
print('张三' in scores)
print('张三' not in scores)

del scores['张三']  # 删除指定的 key-value 对
# scores.clear()  # 清空字典的元素
print(scores)
scores['赵六'] = 520  # 新增元素
print(scores)
scores['李四'] = 100  # 修改元素
print(scores)
