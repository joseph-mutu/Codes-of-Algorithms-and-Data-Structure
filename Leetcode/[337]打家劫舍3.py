#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-07 18:54:16
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.memo = {}
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if root in self.memo:
            return self.memo[root]

        if root.left:
            rob_cur_1 = self.rob(root.left.left) 
            rob_cur_2 = self.rob(root.left.right)
        else:
            rob_cur_1,rob_cur_2 = 0,0
        
        if root.right:
            rob_cur_3 = self.rob(root.right.left)
            rob_cur_4 = self.rob(root.right.right)
        else:
            rob_cur_3,rob_cur_4 = 0,0
        
        rob_cur = root.val + rob_cur_1 + rob_cur_2 + rob_cur_3 +rob_cur_4
        rob_not_cur = self.rob(root.left) +self.rob(root.right)
        res = max(rob_cur,rob_not_cur)
        self.memo[root] = res
        return res

root = TreeNode(3)
node1 = TreeNode(2)
node2 = TreeNode(3)
node3 = TreeNode(3)
node4 = TreeNode(1)
root.left = node1
root.right = node2  
node1.right = node3
node2.right = node4
s = Solution()
print(s.rob(root))