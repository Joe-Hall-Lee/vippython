# 创建星座的列表
constellation = ['白羊座', '金牛座', '双子座', '巨蟹座', '狮子座',
                 '处女座', '天秤座', '天蝎座', '射手座', '摩羯座', '水瓶座', '双鱼座']
word = ['我要', '我有', '我变', '我觉得', '我决定', '我分析',
        '我想', '我渴望', '我追求', '我作', '我了解', '我给']

# 将两个列表转成集合
d = dict(zip(constellation, word))
'''
for item in d:
    print(item,d[item])
'''
print(d)
key = input('情输入您的星座名称')
flag = True
for item in d:
    if key == item:
        flag = True
        print(key, '的专属词汇为:', d.get(key))
        break
    else:
        # print('对不起，您输入的星座有误'）
        flag = False

if not flag:
    print('对不起，您输入的星座有误')
