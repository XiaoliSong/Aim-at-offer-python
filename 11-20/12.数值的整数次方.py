'''
题目描述
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。

解题思路
一、直接返回 base**exponen
二、一维数组分别保存base的1，2，4，8，....2^31 次方，然后exponent对应二进制位为1则乘上，注意exponent为负的情况
'''
'''
# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        return base**exponent
'''


# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if exponent == 0:
            return 1
        arr = [base]
        i = 1
        while i < 32:
            arr.append(arr[-1] * base)
            i += 1

        if exponent < 0:
            positive = False
            exponent = -exponent
        else:
            positive = True
        res = 1
        i = 0
        while i < 32:
            if exponent & 1:
                res *= arr[i]
            exponent = exponent >> 1
            i += 1
        if not positive:
            res = 1 / res
        return res