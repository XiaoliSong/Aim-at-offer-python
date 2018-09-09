'''
题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

解题思路
类似斐波那契数列。n<=1 时, f(n)=1;n>1,f(n)=f(n-1)+f(n-2)
扩展：如果一次可以跳上1级台阶，也可以跳上2级，也可以跳上3级呢？
'''

# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        n = number
        if n <= 1:
            return 1
        else:
            pre1 = 1
            pre2 = 1
            n -= 1
            while n > 0:
                pre1, pre2 = pre2, pre2 + pre1
                n -= 1
            return pre2