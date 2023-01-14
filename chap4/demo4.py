'''会员 >=200 8折
       ＞=100 9折
             不打折
    非会员 >=200 9.5折
                不打折'''
answer = input('您是会员吗？y/n')
money = float(input('写出您的购物金额：'))
# 外层判断是否是会员
if answer == 'y':  # 会员
    if money >= 200:
        print('打八折，付款金额为：', money*0.8)
    elif money >= 100:
        print('打九折，付款金额为：', money*0.9)
    else:
        print('不打折，付款金额为：', money)
else:  # 非会员
    if money >= 200:
        print('打9.5折，付款金额为：', money * 0.95)
    else:
        print('不打折，付款金额为：', money)
