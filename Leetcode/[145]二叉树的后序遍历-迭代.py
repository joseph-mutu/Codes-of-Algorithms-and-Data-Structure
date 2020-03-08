#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-07 10:08:33
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os



class Solution(object):
    def postorderTraversal(self, root):
        if not root:
            return []

        V,NV = 0,1
        node_stack = [(NV,root)]
        postorder = []
        while node_stack:
            status,node = node_stack.pop()
            if node is None:
                continue
            if status == NV:
                node_stack.append((V,node))
                node_stack.append((NV,node.right))
                node_stack.append((NV,node.left))
            else:
                postorder.append(node.val)
        return postorder

