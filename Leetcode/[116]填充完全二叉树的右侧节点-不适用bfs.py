#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-23 08:22:26
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

        leftmost = root

        while leftmost.left:

            head = leftmost

            while head:
                #connect two children
                head.left.next = head.right
                #connect two nodes that belong to two parents
                if head.next:
                    head.right.next = head.next.left
                head = head.next

            leftmost = leftmost.left

        return root

