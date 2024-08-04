import math


class Circle(object):
    def __init__(self, r):
        self.r = r

    def get_area(self):
        return math.pi * math.pow(self.r, 2)

    def get_perimeter(self):
        return 2 * math.pi * self.r


if __name__ == '__main__':
    r = int(input('请输入圆的半径：'))
    c = Circle(r)
    print(f'圆的面积为：{c.get_area()}')
    print(f'圆的周长为：{c.get_perimeter()}')

    print('圆的面积为：{:.2f}'.format(c.get_area()))
    print('圆的周长为：{:.2f}'.format(c.get_perimeter()))
