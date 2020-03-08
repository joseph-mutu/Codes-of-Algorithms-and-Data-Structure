#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-07 09:51:52
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def __init__(self):
        self.preorder = []
    def preorderTraversal(self, root):
        if not root:
            return []
        self.preorder.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)

        return self.preorder