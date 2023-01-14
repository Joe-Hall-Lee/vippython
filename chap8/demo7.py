'''两个集合是否相等(元素相同就相等）'''
s = {12, 4, 5, 56}
s2 = {5, 12, 56, 4}
print(s == s2)  # True
print(s != s2)  # False
'''一个集合是否是另一个集合的子集'''
s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
s2 = {1, 2, 3, 4, 5}
s3 = {1, 2, 4, 90}
print(s2.issubset(s1))  # True
print(s3.issubset(s1))  # False

'''一个集合是否是另一个集合的超集'''
print(s1.issuperset(s2))  # True
print(s2.issuperset(s3))  # False

'''两个集合是否没有交集'''
print(s1.isdisjoint(s2))  # False  有交集为False
s4 = {100, 200, 300}

print(s2.isdisjoint(s4))  # True  没有交集为True
