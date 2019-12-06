'''
today's tasks
    task1: 筛选出运算符
    task2: 根据task1中的运算符分割输入字串
    task3: 打印运算结果
'''
from typing import List, Any


def subtract(c,d):
    return c-d


def multiply(c,d):
    return c*d


def divide(c,d):
    return c/d


def add(c,d):
    return c+d


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
            if arg == "-":
                print(subtract(a,b))
            if arg == "*":
                print(multiply(a,b))
            if arg == "/":
                print(divide(a,b))
