def find_answer(question):
    with open('replay.txt', 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:  # if line=='': 到文件末尾退出
                break
            # 字符串的分割
            keyword = line.split('|')[0]
            reply = line.split('|')[1]
            if keyword in question:
                return reply
    return False


if __name__ == '__main__':
    question = input('您好，欢迎光顾评书新势力SK书场，您可以询问有关书场的任何问题。')
    while True:
        if question == '再见':
            break
        # 开始在文件中查找
        replay = find_answer(question)
        if not replay:  # 如果回复的是False， not False-->True
            question = input(
                '抱歉，这里无法解决您的问题，您可以问一些关于书场性质、内容管理、团结法则、权力声明、伙伴关系、制度守则、管理人员、生效声明等问题，退出请输入“再见”。')
        else:
            print(replay)
            question = input(
                '听户，您还可以问一些关于书场性质、内容管理、团结法则、权力声明、伙伴关系、制度守则、管理人员、生效声明等问题，退出请输入“再见”。')
    print('听户再见！')
