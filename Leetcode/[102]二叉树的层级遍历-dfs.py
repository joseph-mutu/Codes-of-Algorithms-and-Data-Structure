#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-26 06:57:59
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []

        level_order = []

        def dfs(node,level):
            """
            level: current level of the node
            """
            if len(level_order) == level:
                # if it is the first time to start from this level
                level_order.append([])
            level_order[level].append(node.val)

            if node.left:
                dfs(node.left,level + 1)
            if node.right:
                dfs(node.right,level + 1)

        dfs(root,0)
        return level_order
s = Solution()
head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(3)
head.right.left = TreeNode(4)
head.right.right = TreeNode(5)
print(s.levelOrder(head))