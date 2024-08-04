name = set()
for i in range(5):
    info = input(f'请输入第 {i + 1} 个平台的名称和用户名：')
    name.add(info)

for item in name:
    print(item)
