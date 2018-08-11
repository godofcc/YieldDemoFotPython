# -*- coding: utf-8 -*-

#@author: weicheng

#@file: gen_func.py

#@time: 2018/08/11


def gen_func():
    yield 1

def fib(index):
    if index <= 2:
        return 1
    else:
        return fib(index-1) + fib(index-2)

def fib2(index):
    re_list = []
    n,a,b = 0,0,1
    while n<index:
        re_list.append(b)
        a,b = b,a+b
        n += 1
    return re_list


def gen_fib(index):
    n, a, b = 0, 0, 1
    while n < index:
        yield b
        a, b = b, a + b
        n += 1

for data in gen_fib(10):
    print (data)

