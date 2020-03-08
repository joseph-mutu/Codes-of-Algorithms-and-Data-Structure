#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-07 09:19:19
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def __init__(self):
        self.inorder = []

    def inorderTraversal(self, root):
        if not root:
            return []
        self.inorderTraversal(root.left)
        self.inorder.append(root.val)
        self.inorderTraversal(root.right)
        return self.inorder


