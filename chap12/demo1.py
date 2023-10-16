class Student:  # Student 为类的名称（类名），由一个或多个单词组成，每个单词的首字母大写，其余小写
    pass


# Python 中一切皆对象。Student 是对象吗？内存有开空间吗？
print(id(Student))  # 1539062986464
print(type(Student))  # <class 'type'>
print(Student)  # <class '__main__.Student'>
