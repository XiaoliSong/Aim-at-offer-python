'''
题目描述
输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。

解题思路
用一个数组保存遍历结果，然后反转数组
'''


# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if listNode is None:
            return []
        res = []
        while listNode is not None:
            res.append(listNode.val)
            listNode = listNode.next
        res.reverse()
        return res