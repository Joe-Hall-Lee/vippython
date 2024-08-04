'''获取字典的元素'''
scores = {'张三': 1, '李四': 2, '王五': 3}
'''第一种方式，使用 [] '''
print(scores['张三'])
# print(scores['3'])  # KeyError: '3'

'''第二种方式，使用 get() 方法'''
print(scores.get('张三'))
print(scores.get('f'))  # None
print(scores.get('f', 99))  # 99 是在查找 'f' 所对的 value 不存在时，提供的一个默认值
