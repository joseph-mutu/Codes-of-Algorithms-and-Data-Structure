#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-07 10:06:28
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def __init__(self):
        self.postorder = []
    def postorderTraversal(self, root):
        if not root:
            return []

        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        self.postorder.append(root.val)

        return self.postorder