#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-13 08:34:49
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
# Definition for a binary tree node.
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
        def dfs(string,root):
            if not root:
                string += "#,"
                return string

            string += str(root.val)
            string += ','

            string = dfs(string,root.left)
            string = dfs(string,root.right)

            return string
        return dfs("",root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def do_deseralize(nodes):
            if not nodes:
                return
            if nodes[0] == '#':
                nodes.pop(0)
                return

            root = TreeNode(int(nodes[0]))
            nodes.pop(0)
            root.left = do_deseralize(nodes)
            root.right = do_deseralize(nodes)

            return root



        data = data.split(',')[:-1]
        return do_deseralize(data)



s = Codec()
root = TreeNode(1)
root.left =TreeNode(2)
root.right =TreeNode(3)
root.left.left = TreeNode(4)
string = s.serialize(root)
root = s.deserialize(string)
print(root.val)
print(root.left.val)
print(root.right.val)
print(root.left.left.val)

