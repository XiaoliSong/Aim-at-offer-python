'''
题目描述
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。

解题思路
一、移位法，n & 1，n右移
二、n-1法，n = n &(n-1)，直到n为0
'''

# -*- coding:utf-8 -*-
'''
class Solution:
    def NumberOf1(self, n):
        cnt = 0
        i = 0
        while i<32:
            cnt +=  n & 1
            n = n >> 1
            i += 1
        return cnt
'''


class Solution:
    def NumberOf1(self, n):
        if n < 0:
            # 转为正数
            n = n & 0xffffffff
        cnt = 0
        while n != 0:
            n = n & (n - 1)
            cnt += 1
        return cnt