'''
MycontentMgr 实现了特殊方法 __enter__(), __exit__() 称为该类对象遵守了上下文管理协议
该类对象的实例对象，称为上下文管理器

MycontentMgr()

'''


class MycontentMgr(object):
    def __enter__(self):
        print('enter 方法被调用执行了')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit 方法被调用执行了')

    def show(self):
        print('show 方法被调用执行了')


with MycontentMgr() as file:
    file.show()
