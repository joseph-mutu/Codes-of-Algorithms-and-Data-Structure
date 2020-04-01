#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-01 07:37:12
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
    def minDepth(self, root):
        if not root:
            return 0

        node_stack = [(1,root)]
        min_depth = 0

        while node_stack:
            depth,node = node_stack.pop()
            if not node.left and not node.right:
                min_depth = min(min_depth,depth)
            if node.right:
                node_stack.append((depth + 1,node.right))
            if node.left:
                node_stack.append((depth+1,node.left))
        return min_depth
