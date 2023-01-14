'''不可变序列，可变序列'''
lst = [10, 20, 40]
print(id(lst))
lst.append(9)
print(id(lst))
'''不可变序列，字符串，元组'''
s = 'hello'
print(id(s))
s = s+'world'
print(id(s))
print(s)
