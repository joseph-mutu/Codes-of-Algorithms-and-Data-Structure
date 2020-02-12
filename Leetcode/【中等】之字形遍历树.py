#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-12 09:31:11
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution():
    def zigzagLevelOrder(self,root):
        if root is None:
            return []
        stack1 = []
        stack2 = []

        zig_order = []
        stack1.append(root)

        while stack1 or stack2:
            if stack1:
                tem_order = []
                while stack1:
                    tem = stack1.pop()
                    tem_order.append(tem.val)
                    if tem.left:
                        stack2.append(tem.left)
                    if tem.right:
                        stack2.append(tem.right)
                zig_order.append(tem_order)
            else:
                tem_order = []
                while stack2:
                    tem = stack2.pop()
                    tem_order.append(tem.val)
                    if tem.right:
                        stack1.append(tem.right)
                    if tem.left:
                        stack1.append(tem.left)
                zig_order.append(tem_order)
        return zig_order

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
s = Solution()
print(s.zigzagLevelOrder(root))

