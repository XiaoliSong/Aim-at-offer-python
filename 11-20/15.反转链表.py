'''
题目描述
输入一个链表，反转链表后，输出新链表的表头

遍历链表头插法、或者改写原来的链表
'''


# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if pHead is None or pHead.next is None:
            return pHead
        cur = pHead
        cur_next = cur.next
        while cur_next is not None:
            t = cur_next.next
            cur_next.next = cur
            cur = cur_next
            cur_next = t
        pHead.next = None
        return cur