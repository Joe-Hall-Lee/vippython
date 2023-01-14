class Car(object):
    def __init__(self, type, no):
        self.type = type
        self.no = no

    def start(self):
        pass

    def stop(self):
        pass


class Taxi(Car):
    def __init__(self, type, no, company):
        super().__init__(type, no)
        self.company = company

    def start(self):
        print('乘客您好！')
        print(f'我是{self.company}出租车公司的，我的车牌是{self.no}，请问您要去哪里？')

    def stop(self):
        print('目的地到了，请您付款下车，欢迎再次乘坐。')


class FamilyCar(Car):
    def __init__(self, type, no, name):
        super().__init__(type, no)
        self.name = name

    def stop(self):
        print('目的地到了，我们一起去玩吧！')

    def start(self):
        print(f'我是{self.name},我的汽车我做主！')


if __name__ == '__main__':
    taxi = Taxi('上海大众', '京A9765', '长城')
    taxi.start()
    taxi.stop()
    print('—'*30)
    familycar = FamilyCar('广汽丰田', '京B8888', '武大郎')
    familycar.start()
    familycar.stop()
