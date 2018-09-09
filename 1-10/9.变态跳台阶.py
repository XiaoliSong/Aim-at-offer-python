'''
题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

解题思路
f(n) = f(n-1) + f(n-2) + f(n-3) +  ....
'''

# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        n = number
        if n < 1:
            return 1
        arr = [1,1]
        n -= 1
        while n > 0:
            arr.append(sum(arr))
            n -= 1
        return arr[-1]
