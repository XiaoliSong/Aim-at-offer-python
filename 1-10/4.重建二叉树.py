'''
题目描述
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。

解题思路
前序遍历第一个节点为根节点，然后在中序遍历中找出该节点，则可以找出根节点的左边节点个数，右边节点个数。然后递归重建
'''


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if len(pre) == 0:
            return None
        val = pre[0]
        root = TreeNode(val)
        index = tin.index(val)
        root.left = self.reConstructBinaryTree(pre[1:index + 1], tin[0:index])
        root.right = self.reConstructBinaryTree(pre[index + 1:],
                                                tin[index + 1:])
        return root