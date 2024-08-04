def fun(*args):  # 函数定义时的可变函数
    print(args)
    # print(args[0])


fun(10)
fun(10, 30)
fun(30, 405, 50)


def fun1(**args):
    print(args)


fun1(a=10)
fun1(a=20, b=30, c=40)

print('hello', 'world', 'Python')

'''
def fun2((*args, *a):
    pass
以上代码，程序会报错，个数可变的位置参数，只能是 1 个
    def fun2((**args1, **args2)):
    pass
以上代码，程序会报错，个数可变的关键字参数，只能是 1 个
'''


def fun2(*args1, **args2):
    pass


'''def fun3(**args1,*args2)
   pass
   在一个函数的定义过程中，既有个数可变的关键字形参，也有个数可变的位置形参，要求，个数可变的位置形参，放在个数可变的关键字形参之前
'''
