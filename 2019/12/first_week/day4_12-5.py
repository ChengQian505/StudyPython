'''
today's tasks
    task1: 筛选出运算符
    task2: 根据task1中的运算符分割输入字串
    task3: 打印运算结果
'''
import re

def subtract(c,d):
    return c-d


def multiply(c,d):
    return c*d


def divide(c,d):
    return c/d


def add(c,d):
    return c+d


def calculator1():
    args=["+","-","*","/"]
    while 1:
        s=input("请输入:")
        for arg in args:
            arg1=s.split(arg,2)
            if arg1.__len__()==2:
                a=float(arg1[0])
                b=float(arg1[1])
                if arg == "+":
                    print(add(a,b))
                elif arg == "-":
                    print(subtract(a,b))
                elif arg == "*":
                    print(multiply(a,b))
                elif arg == "/":
                    print(divide(a,b))


#进阶版 使用正则操作
def calculator():
    while 1:
        s=input("请输入:")
        arg=re.findall(r'[+\-*/%]',s)
        if not arg.__len__()==1:
            print("目前只支持单个运算符")
            continue
        arg=arg[0]
        arg1 = s.split(arg, 2)
        a = float(arg1[0])
        b = float(arg1[1])
        if arg == "+":
            print(add(a, b))
        elif arg == "-":
            print(subtract(a, b))
        elif arg == "*":
            print(multiply(a, b))
        elif arg == "/":
            print(divide(a, b))
        elif arg == "%":
            print(a % b)


calculator()
