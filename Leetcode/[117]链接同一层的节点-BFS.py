#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-11 06:55:19
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root

        node_stack = [root]

        while node_stack:
            cur_length = len(node_stack)
            while cur_length:
                node = node_stack.pop(0)
                if node.left:
                    node_stack.append(node.left)
                if node.right:
                    node_stack.append(node.right)
                if cur_length > 1:
                    node.next = node_stack[0]
                cur_length -= 1
        return root