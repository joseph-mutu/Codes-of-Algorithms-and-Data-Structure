#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-13 19:35:13
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.max_sum = float('-inf')
        self.dfs(root)
        return self.max_sum
    
    def dfs(self,root):
        if not root:
            return None
        left_sum = self.dfs(root.left)
        right_sum = self.dfs(root.right)

        if left_sum and left_sum > self.max_sum:
            self.max_sum = left_sum
        if right_sum and right_sum > self.max_sum:
            self.max_sum = right_sum


        if root.val + left_sum + right_sum > self.max_sum:
            self.max_sum = root.val + left_sum + right_sum
        return max(left_sum,right_sum) + root.val

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
head = TreeNode(-3)
s = Solution()
print(s.maxPathSum(head))