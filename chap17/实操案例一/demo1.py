'''一、使用 print 方式进行输出（输出的目的地是文件）'''
fp = open('F:\\CS\\Python\\vippython\\chap17\\实操案例一\\test.txt', 'w')
print('奋斗成就更好的你', file=fp)
fp.close()

'''第二种方式，使用文件读写操作'''
with open('F:\\CS\\Python\\vippython\\chap17\\实操案例一\\test1.txt', 'w') as file:
    file.write('奋斗成就更好的你')
