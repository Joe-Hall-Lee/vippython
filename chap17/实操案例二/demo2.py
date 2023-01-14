'''1.变量的赋值'''
name1 = '《三国前传(SK)》'
name2 = '《三国正传(SK)》'
name3 = '《水浒全传(SK)》'
name4 = '《东周列国志(SK)》'
name5 = '《戏说镜花缘之唐氏大仙传(SK)》'
print('①\t'+name1)
print('②\t'+name2)
print('③\t'+name3)
print('④\t'+name4)
print('⑤\t'+name5)
print('--------------------------------------')
'''第2种方式'''
lst_name = ['《三国前传(SK)》', '《三国正传(SK)》', '《水浒全传(SK)',
            '《东周列国志(SK)》', '《戏说镜花缘之唐氏大仙传(SK)》']
lst_sig = ['①', '②', '③', '④', '⑤']
for i in range(5):
    print(lst_sig[i], lst_name[i])
print('---------------------------------------')
'''3.字典'''
d = {'①': '《三国前传(SK)》', '②': '《三国正传(SK)》', '③': '《水浒全传(SK)',
     '④': '《东周列国志(SK)》', '⑤': '《戏说镜花缘之唐氏大仙传(SK)》'}
for key in d:
    print(key, d[key])
print('zip------------------------------------')
for s, name in zip(lst_sig, lst_name):
    print(s, name)
