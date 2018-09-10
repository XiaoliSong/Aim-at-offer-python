'''
题目描述
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。

解题思路：
奇偶两个数组，然后合并
'''
'''
# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        odd_arr = []
        even_arr = []
        for x in array:
            if x & 1:
                odd_arr.append(x)
            else:
                even_arr.append(x)
                
        return odd_arr+even_arr
'''


# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        return sorted(array, key=lambda c: c % 2, reverse=True)
