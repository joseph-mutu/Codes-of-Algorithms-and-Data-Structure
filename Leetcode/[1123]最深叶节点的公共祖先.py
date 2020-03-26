#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-26 19:16:13
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
    def lcaDeepestLeaves(self, root):
        if not root:
            return None
        depth,node = self.search(root)
        return node.val

    
    def search(self,root):
        if not root:
            return 0,None
        left_depth,left_node = self.search(root.left)
        right_depth, right_node = self.search(root.right)
        
        if left_depth > right_depth:
            return left_depth + 1,left_node
        elif left_depth == right_depth:
            return left_depth + 1, root
        elif right_depth > left_depth:
            return right_depth + 1, right_node


s = Solution()
head = TreeNode(1)
left = TreeNode(2)
right = TreeNode(3)
left.left = TreeNode(4)
head.left = left
head.right = right
print(s.lcaDeepestLeaves(head))