'''
题目描述
输入一个链表，输出该链表中倒数第k个结点。

解题思路
快慢指针，快指针先走k步，然后快慢指针同时走，快指针走到尾时则慢指针此时指向倒数第k个结点
'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        fast = head
        i = 0
        while i < k:
            if fast is None:
                return None
            i += 1
            fast = fast.next

        slow = head
        while fast is not None:
            fast = fast.next
            slow = slow.next
        return slow