#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-14 19:24:39
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
    def convertBST(self, root: TreeNode) -> TreeNode:
        def dfs(root,tem_sum):
            if not root:
                return 0
            if not root.left and not root.right:
                record = root.val
                root.val += tem_sum
                return record

            root.val += tem_sum

            right = dfs(root.right,tem_sum)
            root.val += right
            left = dfs(root.left,root.val)

            return root.val + left
        dfs(root,0)
        return root

s = Solution()
root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(-3)
root.left.left.left = TreeNode(-1)
root.left.left.left.left = TreeNode(0)
nr = s.convertBST(root)

print(nr.left.val)



