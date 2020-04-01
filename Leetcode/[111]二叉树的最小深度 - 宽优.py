#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-01 07:56:47
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
    def minDepth(self, root):
        if not root:
            return 0

        node_stack = [(1,root)]
        while node_stack:
            depth,node = node_stack.pop(0)
            if not node.left and not node.right:
                return depth
            if node.left:
                node_stack.append((depth+1,node.left))
            if node.right:
                node_stack.append((depth+1,node.right))
                