'''
题目描述
请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''

'''
解题思路

遍历字符串然后遇到空格替换
'''

# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        res = ''
        for c in s:
            if c == ' ':
                res += '%20'
            else:
                res += c
        return res