'''
题目描述
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）

解题思路
树的子结构是指pRoot1包含pRoot2
'''


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsSubTree(self, pRoot1, pRoot2):
        if pRoot2 is None:
            return True
        if pRoot1 is None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.IsSubTree(pRoot1.left, pRoot2.left) and self.IsSubTree(
            pRoot1.right, pRoot2.right)

    def HasSubtree(self, pRoot1, pRoot2):
        flag = False
        if pRoot1 is not None and pRoot2 is not None:
            if pRoot1.val == pRoot2.val:
                flag = self.IsSubTree(pRoot1.left,
                                      pRoot2.left) and self.IsSubTree(
                                          pRoot1.right, pRoot2.right)
            if not flag:
                flag = self.IsSubTree(pRoot1.left, pRoot2)
            if not flag:
                flag = self.IsSubTree(pRoot1.right, pRoot2)
            return flag
        else:
            return flag
