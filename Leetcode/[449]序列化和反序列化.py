#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-10 10:13:39
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # 使用后序遍历存储
        V,NV = 1, 0
        postorder = []
        node_stack = [(NV,root)]

        while node_stack:
            vis,node = node_stack.pop()
            if node is None:
                continue
            if vis == NV:
                node_stack.append((V,node))
                node_stack.append((NV,node.right))
                node_stack.append((NV,node.left))
            else:
                postorder.append(node.val)
        return " ".join(map(str,postorder))
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # 从后序遍历中复原二叉搜索树

        def helper(lower = float('-inf'),upper = float('inf')):
            if not data or data[-1] < lower or data[-1] > upper:
                return None
            value = data.pop()
            root = TreeNode(value)

            root.left = helper(lower,value)
            root.right = helper(value,upper)
            return root
        data = [int(i) for i in data.split(' ')]
        return helper()

