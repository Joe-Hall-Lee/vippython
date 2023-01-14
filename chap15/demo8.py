file = open('c.txt', 'a')
# file.write('hello')
lst = ['java', 'go', 'python']
file.writelines(lst)
file.close()
