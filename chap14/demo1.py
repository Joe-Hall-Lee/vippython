def fun():
    pass


def fun2():
    pass


class Student:
    nativeplace = '吉林'  # 类属性

    def eat(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def cm(cls):
        pass

    @staticmethod
    def sm():
        pass


a = 10
b = 20
print(a+b)
