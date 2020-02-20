#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-14 07:13:02
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
    def isValidBST(self, root):
        if not root:
            return True

        inorder = []
        pre = float('-inf')

        while inorder or root:
            while root:
                inorder.append(root)
                root = root.left
            root = inorder.pop()
            if root.val <= pre:
                return False
            pre = root.val
            root = root.right

        return True




