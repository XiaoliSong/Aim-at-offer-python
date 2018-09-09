'''
题目描述
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

解题思路：
旋转数组符合↗ ↗增减情况，所以遍历出第一个比左边小的元素即可
'''
# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        elif len(rotateArray) == 1:
            return rotateArray[0]
        
        i = 1
        while i < len(rotateArray):
            if rotateArray[i-1] > rotateArray[i]:
                return rotateArray[i]
            i+=1