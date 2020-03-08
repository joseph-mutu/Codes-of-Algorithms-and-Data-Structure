#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-07 09:35:13
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def preorderTraversal(self, root):
        V,NV = 1,0

        node_stack = [(NV,root)]
        res = []
        while node_stack:
            status,node = node_stack.pop()
            if node is None:
                continue
            if status == NV:
                # 入栈
                node_stack.append((NV,node.right))
                node_stack.append((NV,node.left))
                node_stack.append((NV,node))
            else:
                res.append(node.val)
        return res