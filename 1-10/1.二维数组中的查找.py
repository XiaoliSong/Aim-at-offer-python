'''
题目描述
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数
'''

'''
解题思路

最小→
↓   
        最大

二维数组满足上面的样子，所以从右上角开始比较，比target大，j--，比target小i++；当然从左下角开始比较也是可以的
'''

# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        h = len(array)
        if h <= 0:
            return False
        w = len(array[0])
        i = 0
        j = h-1
        while i < w and j >=0:
            if array[i][j] == target:
                return True
            elif array[i][j] > target:
                j-=1
            else:
                i+=1
        return False