import copy


class CPU:
    pass


class DISK:
    pass


class Computer:
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk


# （1）变量的赋值
cpu1 = CPU()
cpu2 = cpu1
print(cpu1, id(cpu1))
print(cpu2, id(cpu2))
# （2）类的浅拷贝
print('--------------------------------------')
disk = DISK()  # 创建一个硬盘类的对象
computer = Computer(cpu1, disk)  # 创建一个计算机类的对象

# 浅拷贝
print(disk)
computer2 = copy.copy(computer)
print(computer, computer.cpu, computer.disk)
print(computer2, computer2.cpu, computer2.disk)
print('--------------------------------------------')
# 深拷贝
computer3 = copy.deepcopy(computer)
print(computer, computer.cpu, computer.disk)
print(computer3, computer3.cpu, computer3.disk)
