# 集合的相关操作
s = {10.2, 30, 440}
# 集合元素的判断操作
print(10 in s)  # False
print(100 in s)  # False
print(100 not in s)  # True
print(10 not in s)  # True
'''集合元素的新增操作'''
s.add(80)  # add一次添加一个元素
print(s)
s.update({13, 79, 86})  # 一次至少添加一个元素
print(s)
s.update([177, 57, 8])
s.update((67, 98, 9))
print(s)

'''集合元素的删除操作'''
s.remove(80)
print(s)
# s.remove(667)  # KeyError: 667
s.discard(4)
s.discard(5)
print(s)
s.pop()
s.pop()
# s.pop(6)  # TypeError: pop() takes no arguments (1 given)
print(s)
s.clear()
print(s)
