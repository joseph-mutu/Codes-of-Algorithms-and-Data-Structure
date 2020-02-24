#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-23 07:55:17
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution(object):
    def connect(self, root):
        if not root:
            return None
        bfs = []

        size = 0

        bfs.append(root)

        while bfs:

            size = len(bfs)

            for i in range(size):
                node = bfs.pop(0)

                if node.left:
                    bfs.append(node.left)
                    bfs.append(node.right)

                if bfs and i != size - 1:
                    node.next = bfs[0]
                else:
                    continue

        return root
s = Solution()


