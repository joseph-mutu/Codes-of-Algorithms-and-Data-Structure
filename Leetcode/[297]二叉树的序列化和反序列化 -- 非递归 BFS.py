#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-13 08:53:24
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
        nodes = [root]
        string = ""

        while nodes:
            node = nodes.pop(0)
            if node is None:
                string += "#,"
                continue
            else:
                string += str(node.val)
                string += ','
            nodes.append(node.left)
            nodes.append(node.right)
        return string
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def do_deserialize(self,length):
            

s = Codec()
root = TreeNode(1)
root.left =TreeNode(2)
root.right =TreeNode(3)
root.left.left = TreeNode(4)
string = s.serialize(root)
print(string)