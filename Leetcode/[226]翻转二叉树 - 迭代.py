#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-01 08:02:29
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def invertTree(self, root):
        if not root:
            return None
        # 后序遍历
        node_stack = [(1,root)]

        while node_stack:
            vis,node = node_stack.pop()
            if not node:
                continue
            if not node.left and not node.right:
                continue
            if vis == 1:
                node_stack.append((0,node))
                node_stack.append((1,node.right))
                node_stack.append((1,node.left))
            elif vis == 0:
                tem = node.left
                node.left = node.right
                node.right = tem
        return root
