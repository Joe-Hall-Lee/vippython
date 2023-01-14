pwd = input('请输入支付密码：')
if pwd.isdigit():
    print('支付数据合法')
else:
    print('支付数据不合法，支付密码只能是数字')

print('----------------------------------------------')
print('支付数据不合法' if pwd.isdigit() else '支付数据不合法，支付密码只能是数字')
