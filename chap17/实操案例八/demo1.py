版块 = ('书场管理', '相声段子', '评书艺术', '京剧国粹', '经典鼓曲', '小曲小调', '快板说唱', '德云天团')
print('您好，欢迎光临评书新势力SK书场超话！')
print('书场超话的版块分区有：')
for index, item in enumerate(版块):
    print(index + 1, '.', item, end=' ')

index = int(input('\n请输入您感兴趣的版块分区编号：'))
if 0 <= index < len(版块):
    print(f'您现在可以看【{版块[index - 1]}】了！')
1
