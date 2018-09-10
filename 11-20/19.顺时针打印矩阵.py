'''
题目描述
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.

解题思路
遍历输出，注意矩阵可能不是方阵，最后只剩下一行、一列的特殊情况
'''


# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        res = []
        if len(matrix) == 0:
            return res
        left = top = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1

        while left <= right and top <= bottom:
            # 第一行
            res = res + matrix[top][left:right + 1]
            # 最后一列
            i = top + 1
            while i <= bottom:
                res.append(matrix[i][right])
                i += 1

            if top != bottom:
                # 最后一行
                j = right - 1
                while j >= left:
                    res.append(matrix[bottom][j])
                    j -= 1

            if left != right:
                # 第一列
                i = bottom - 1
                while i > top:
                    res.append(matrix[i][left])
                    i -= 1
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return res