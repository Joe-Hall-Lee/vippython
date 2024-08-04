'''
多分支结构，多选一执行
从键盘录入一个整数（成绩）
90-100 A
80-89 B
70-79 C
60-69 D
0-59 E
小于 0 或大于 100 的为非法数据（不是成绩的有效范围）
'''
score = int(input('请输入一个成绩：'))
# 判断
if score >= 90 and score <= 100:
    print('A 级')
elif score >= 80 and score <= 89:
    print('B 级')
elif score >= 70 and score <= 79:
    print('C 级')
elif score >= 60 and score <= 69:
    print('D 级')
elif score >= 0 and score <= 59:
    print('E 级')
else:
    print('对不起，成绩有误，不在成绩的有效范围')
