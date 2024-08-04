class Person(object):

    def __new__(cls, *args, **kwargs):
        print('__new__ 被调用执行了，cls 的 id 值为：{0}'.format(id(cls)))
        obj = super().__new__(cls)
        print('创建的对象的 id 为：{}'.format(id(obj)))
        return obj

    def __init__(self, name, age):
        print('__init__ 被调用了，self 的 id 值为：{0}'.format(id(self)))
        self.name = name
        self.age = age


print('object 这个类对象的 id 为：{0}'.format(id(object)))
print('Person 这个类对象的 id 为：{0}'.format(id(Person)))

# 创建 Person 类的实例对象
p1 = Person('张三', 20)
print('p1 这个 Person 类的实例对象的 id：{0}'.format(id(p1)))
