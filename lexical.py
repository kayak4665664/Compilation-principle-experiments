import re
x = open('source.txt', 'r', encoding='utf-8')
e = x.read()  # 打开并读入文件
p = '//.*|\/\*(?:[^\*]|\*+[^\/\*])*\*+\/'  # 用于预处理中匹配注释的正则表达式
e = re.sub(' +', ' ', re.sub(p, '', e).replace('\\\n', '').replace('\n', ' '))
x = open('预处理.txt', 'w', encoding='utf-8')
x.write(e)  # 写入预处理文件
x = open('二元式表.txt', 'w', encoding='utf-8')
k = ['IF', 'THEN', 'ELSE', 'GOTO']
o = ['+', '-', '*', '/', '>', '<', '=', '>=', '<=', '<>']
p = [',', '(', ')', ':']
s = ''  # 单词
f = False  # 判断是否为标号
for i in range(len(e)):  # 从左到右扫描源程序
    s += e[i]
    if i < len(e) - 1:
        c = e[i + 1]
    else:
        c = ' '
    t = s + c
    if t not in k and t not in o and t not in p and t.isidentifier() == False and t.isdigit() == False:
        if (f == True or c == ':') and s.isdigit() == True:  # 识别为标号
            x.write('(L,' + s + ')\n')
            f = False
        elif s.isdigit() == True:  # 识别为常数
            x.write('(C,' + s + ')\n')
        elif s in k:  # 识别为关键字
            x.write('(K,' + s + ')\n')
            if s == 'GOTO':
                f = True
        elif s in o:  # 识别为运算符
            x.write('(O,' + s + ')\n')
        elif s in p:  # 识别为界符
            x.write('(P,' + s + ')\n')
        elif s.isidentifier() == True:  # 识别为标识符
            x.write('(I,' + s + ')\n')
        s = ''