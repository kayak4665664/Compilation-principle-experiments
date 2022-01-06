# Compilation-principle-experiments
These programs are experiments in the Compilation principle course of the Computer Department of North China University of Technology.  
这是程序是北方工业大学计算机系编译原理实验。

Time: 2021 Spring Semester

## `lexical.py` 词法分析
K(keyword 关键字), I(identifier 标识符), C(constant 常数), P(separator 界符), L(label 标号), O(operator 操作符)
1. input: `source.txt`  
```
/*example*/
    b=1\
00
101:a=2*(1+3)
    IF(b>10) THEN
        a=1
    ELSE IF(b>=5) THEN
        a=2
    ELSE
        GOTO 101
```
2. output: `预处理.txt`(pre-processing), `二元式表.txt`
```
 b=100 101:a=2*(1+3) IF(b>10) THEN a=1 ELSE IF(b>=5) THEN a=2 ELSE GOTO 101
```
```
(I,b)
(O,=)
(C,100)
(L,101)
(P,:)
(I,a)
(O,=)
(C,2)
(O,*)
(P,()
(C,1)
(O,+)
(C,3)
(P,))
(K,IF)
(P,()
(I,b)
(O,>)
(C,10)
(P,))
(K,THEN)
(I,a)
(O,=)
(C,1)
(K,ELSE)
(K,IF)
(P,()
(I,b)
(O,>=)
(C,5)
(P,))
(K,THEN)
(I,a)
(O,=)
(C,2)
(K,ELSE)
(K,GOTO)
(L,101)
```

## `grammar.py` 语法分析
1. input: `预处理.txt`
```
 b=100 101:a=2*(1+3) IF(b>10) THEN a=1 ELSE IF(b>=5) THEN a=2 ELSE GOTO 101
```
2. output: 
```
算术表达式 0 为： 100
转换为输入串： i#
步骤号   符号栈   优先关系   当前分析符   剩余输入串   动作
0        #                                i#           预备  
1        #i       <          i            #            移进  
2        #N       >          N            #            规约  
3        #N#      =          #                         移进  
算术表达式 0 的规约产生式步骤号为： 2
-----------------------------------------------------------
算术表达式 1 为： 2*(1+3)
转换为输入串： i*(i+i)#
步骤号   符号栈   优先关系   当前分析符   剩余输入串   动作
0        #                                i*(i+i)#     预备  
1        #i       <          i            *(i+i)#      移进  
2        #N       >          N            *(i+i)#      规约  
3        #N*      <          *            (i+i)#       移进  
4        #N*(     <          (            i+i)#        移进  
5        #N*(i    <          i            +i)#         移进  
6        #N*(N    >          N            +i)#         规约  
7        #N*(N+   <          +            i)#          移进  
8        #N*(N+i  <          i            )#           移进  
9        #N*(N+N  >          N            )#           规约  
10       #N*(N    >          N            )#           规约  
11       #N*(N)   <          )            #            移进  
12       #N*N     >          N            #            规约  
13       #N       >          N            #            规约  
14       #N#      =          #                         移进  
算术表达式 1 的规约产生式步骤号为： 2,6,9,10,12,13
-----------------------------------------------------------
算术表达式 2 为： 1
转换为输入串： i#
步骤号   符号栈   优先关系   当前分析符   剩余输入串   动作
0        #                                i#           预备  
1        #i       <          i            #            移进  
2        #N       >          N            #            规约  
3        #N#      =          #                         移进  
算术表达式 2 的规约产生式步骤号为： 2
-----------------------------------------------------------
算术表达式 3 为： 2
转换为输入串： i#
步骤号   符号栈   优先关系   当前分析符   剩余输入串   动作
0        #                                i#           预备  
1        #i       <          i            #            移进  
2        #N       >          N            #            规约  
3        #N#      =          #                         移进  
算术表达式 3 的规约产生式步骤号为： 2
-----------------------------------------------------------
算符优先语法分析结束！
```