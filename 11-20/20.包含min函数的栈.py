'''
题目描述
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。

解题思路：
一个普通栈、一个保存最小值的栈
入栈时，node<=最小栈的栈顶，最小栈node入栈
出栈时，普通栈栈顶=最小栈的栈顶，最小栈也同时出栈
'''


# -*- coding:utf-8 -*-
class Stack:
    def __init__(self):
        self.__s = []

    def __len__(self):
        return len(self.__s)

    def push(self, node):
        self.__s.append(node)

    def top(self):
        if len(self.__s) == 0:
            return None
        else:
            return self.__s[-1]

    def pop(self):
        return self.__s.pop()


class Solution:
    def __init__(self):
        self.__s = Stack()
        self.__min_s = Stack()

    def push(self, node):
        if len(self.__s) == 0 or node <= self.__min_s.top():
            self.__min_s.push(node)
        self.__s.push(node)

    def pop(self):
        node = self.__s.pop()
        if node == self.__min_s.top():
            self.__min_s.pop()
        return node

    def top(self):
        return self.__s.top()

    def min(self):
        return self.__min_s.top()
