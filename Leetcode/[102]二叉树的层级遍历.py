#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-26 06:45:06
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []

        bfs = [root]
        level_order = []

        while bfs:
            tem = []
            size = len(bfs)
            while size > 0:
                size -= 1
                node = bfs.pop(0)
                if node.left:
                    bfs.append(node.left)
                if node.right:
                    bfs.append(node.right)
                tem.append(node.val)
            level_order.append(tem[:])
        return level_order

s = Solution()
head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(3)
head.right.left = TreeNode(4)
head.right.right = TreeNode(5)
print(s.levelOrder(head))



