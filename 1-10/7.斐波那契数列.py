'''
题目描述
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39

解题思路：
递归比较慢，备忘录递归也比较慢，迭代快
'''

# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        if n <= 1:
            return n
        else:
            pre1 = 0
            pre2 = 1
            n -= 1
            while n > 0:
                pre1, pre2 = pre2, pre2 + pre1
                n -= 1
            return pre2