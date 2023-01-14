class Instrument:
    def make_sound(self):
        pass


class Erhu(Instrument):
    def make_sound(self):
        print('二胡在演奏')


class Piano(Instrument):
    def make_sound(self):
        print('钢琴在演奏')


class Violin(Instrument):
    def make_sound(self):
        print('小提琴在演奏')

# 演奏的函数


def play(Instrument):
    Instrument.make_sound()


class Bird():
    def make_sound(self):
        print('小鸟在唱歌')


if __name__ == '__main__':
    play(Erhu())
    play(Piano())
    play(Violin())
    play(Bird())
