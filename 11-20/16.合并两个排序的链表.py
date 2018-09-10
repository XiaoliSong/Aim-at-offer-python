'''
题目描述
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。

解题思路
两个链表同时遍历并比较然后重建链表
'''


# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        if pHead1 is None:
            return pHead2
        elif pHead2 is None:
            return pHead1
        if pHead1.val > pHead2.val:
            res = head = pHead2
            pHead2 = pHead2.next
        else:
            res = head = pHead1
            pHead1 = pHead1.next

        while pHead1 is not None and pHead2 is not None:
            if pHead1.val > pHead2.val:
                head.next = pHead2
                head = pHead2
                pHead2 = pHead2.next
            else:
                head.next = pHead1
                head = pHead1
                pHead1 = pHead1.next
        if pHead1 is not None:
            head.next = pHead1
        else:
            head.next = pHead2
        return res