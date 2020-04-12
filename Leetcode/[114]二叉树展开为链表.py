#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-11 08:37:53
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 如果当前节点为空或者为根节点，直接返回
        if not root or (not root.left and not root.right):
            return root
        
        record = self.flatten(root.right)
        root.right = None
        left = self.flatten(root.left)
        root.right = left
        root.left = None
        if record is None:
            return root
        else:
            node = root
            while node.right:
                node = node.right
            node.right = record
        return root
        
s = Solution()
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

print(s.flatten(root).right.right.val)
