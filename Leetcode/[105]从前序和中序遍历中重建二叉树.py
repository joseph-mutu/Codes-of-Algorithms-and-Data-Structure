#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-25 06:49:59
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
    def buildTree(self, preorder, inorder):
        if not inorder or not preorder:
            return
        root = TreeNode(preorder[0])

        root_in_index = inorder.index(root.val)

        left_len = len(inorder[0:root_in_index])
        right_len = len(inorder[root_in_index+1:])

        root.left = self.buildTree(preorder[1:1+left_len],inorder[0:left_len])
        root.right = self.buildTree(preorder[left_len + 1:],inorder[root_in_index+1:])

        return root
preorder = []
inorder = []
s = Solution()
print(s.buildTree(preorder,inorder).right.val)