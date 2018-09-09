'''
题目描述
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

解题思路
队列，先进先出FIFO
入队时，s1进栈
出队时，判断s2是否空，s2不空的话出栈返回结果；s2空，则判断s1是否空，s1空则返回None，s1不为空则s1全部元素出栈到s2入栈且最后s2出栈返回结果
'''

# -*- coding:utf-8 -*-

class Stack:
    def __init__(self):
        self.__s = []
    
    def __len__(self):
        return len(self.__s)
    
    def push(self,node):
        self.__s.append(node)
        
    def pop(self):
        return self.__s.pop()

class Solution:
    def __init__(self):
        self.__s1 = Stack()
        self.__s2 = Stack()
    
    def push(self, node):
        self.__s1.push(node)
    
    def pop(self):
        if len(self.__s2) == 0:
            if len(self.__s1) == 0:
                return None
            else:
                while len(self.__s1) > 0:
                    node = self.__s1.pop()
                    self.__s2.push(node)
        return self.__s2.pop()

s = Solution()
s.push(1)
s.push(2)
s.push(3)
print(s.pop())
print(s.pop())