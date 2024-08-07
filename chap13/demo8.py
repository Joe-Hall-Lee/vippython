# print(dir(object))
class A:
    pass


class B:
    pass


class C(A, B):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class D(A):
    pass


# 创建 C 类的对象
x = C('Jack', 20)  # x 是 C 类型的一个实例对象
print(x.__dict__)
print(C.__dict__)
print('---------------------------------')
print(x.__class__)  # <class '__main__.C'> 输出了对象所属的类
print(C.__bases__)  # C 类的父类类型的元素
print(C.__base__)  # 类的基类
print(C.__mro__)  # 类的层次结构
print(A.__subclasses__())  # 子类的列表
