import numpy as np
p = np.array([[1, 1, -1, -1, -1, 1, -1, 1], [1, 1, -1, -1, -1, 1, -1, 1], [1, 1, 1, 1, -1, 1, -1, 1], [1, 1, 1, 1, -1, 1, -1, 1],
             [-1, -1, -1, -1, -1, 0, -1, -2], [1, 1, 1, 1, -2, 1, -2, 1], [1, 1, 1, 1, -2, 1, -2, 1], [-1, -1, -1, -1, -1, -2, -1, 0]])  # 1> -1< 0= 算符优先表
n = {}
l = ['N+N', 'N-N', 'N*N', 'N/N', '(N)']
n['+'] = 0
n['-'] = 1
n['*'] = 2
n['/'] = 3
n['('] = 4
n[')'] = 5
n['i'] = 6
n['#'] = 7
x = open('预处理.txt', 'r', encoding='utf-8')  # 读取词法分析预处理结果
e = x.read()
s = []  # 提取到的算术表达式
a = []  # 算术表达式转换后的输入串
t = ''
f = False
for i in range(len(e)):  # 提取算术表达式
    if e[i] == ' ' and f == True:
        f = False
        s.append(t)
        t = ''
    if f:
        t += e[i]
    if e[i] == '=' and e[i-1] != '<' and e[i-1] != '>':
        f = True
def tran(t):  # 将算术表达式转换为输入串
    r = ''
    f = False
    for c in t:
        if c.isdigit() == False:
            r += c
            f = False
        elif f == False:
            r += 'i'
            f = True
    return r + '#'
for t in s:
    a.append(tran(t))
for i in range(len(s)):  # 语法分析
    print('算术表达式', i, '为：', s[i])
    print('转换为输入串：', a[i])
    k = '#'  # 符号栈
    t = a[i]  # 剩余输入串
    m = []  # 规约产生式步骤
    print('步骤号   符号栈   优先关系   当前分析符   剩余输入串   动作')
    print('%-6d   %-7s  %-8s   %-10s   %-10s   %-4s' % (0, k, '', '', t, '预备'))
    c = int(1)  # 编号
    while len(t) > 0:
        if k[-3:] in l:  # 符号栈倒数3个字符可以继续规约
            k = k[:-3] + 'N'
            m.append(str(c))
            print('%-6d   %-7s  %-8s   %-10s   %-10s   %-4s' %
                  (c, k, '>', k[len(k) - 1], t, '规约'))
        elif k[len(k) - 1] == 'N':  # 对'N'字符特判，进行移进
            if p[n['#'], n[t[0]]] == 0:
                y = '='
            elif p[n['#'], n[t[0]]] == 1:
                y = '>'
            elif p[n['#'], n[t[0]]] == -1:
                y = '<'
            k += t[0]
            t = t[1:]
            print('%-6d   %-7s  %-8s   %-10s   %-10s   %-4s' %
                  (c, k, y, k[len(k) - 1], t, '移进'))
        elif p[n[k[len(k) - 1]], n[t[0]]] == 1:  # 符号栈字符优先级高，进行规约
            if k[len(k) - 1] == 'i':
                k= k[:-1] + 'N'
                m.append(str(c))
                print('%-6d   %-7s  %-8s   %-10s   %-10s   %-4s' %
                  (c, k, '>', k[len(k) - 1], t, '规约'))
        elif p[n[k[len(k) - 1]], n[t[0]]] == 0 or p[n[k[len(k) - 1]], n[t[0]]] == -1:  # 符号栈字符优先级与剩余输入串字符优先级相等或低，进行移进
            k += t[0]
            t = t[1:]
            print('%-6d   %-7s  %-8s   %-10s   %-10s   %-4s' %
                  (c, k, '=' if p[n[k[len(k) - 1]], n[t[0]]] == 0 else '<', k[len(k) - 1], t, '移进'))
        
        c += 1
    print('算术表达式', i, '的规约产生式步骤号为：', ','.join(m))
    print('-----------------------------------------------------------')
print('算符优先语法分析结束！')