'''
题目描述
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

解题思路
类似于斐波那契数列，f(n) = f(n-1) + f(n-2) , n>1时
'''

# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        n = number
        if n <= 1:
            return n
        else:
            pre1 = 1
            pre2 = 1
            n -= 1
            while n > 0:
                pre1, pre2 = pre2, pre2 + pre1
                n -= 1
            return pre2