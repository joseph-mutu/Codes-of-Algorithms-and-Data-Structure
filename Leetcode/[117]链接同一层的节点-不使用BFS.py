#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-11 06:55:51
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
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        
        # leftmost 表示当前层的最左边的节点
        leftmost = root

        while leftmost:
            #  cur 表示当前层正在遍历的节点
            # prev 表示下一层节点中，上一个需要连接的节点
            cur,prev = leftmost,None
            
            # 在遍历过程中将 leftmost 更新为下一层的最左边的节点
            leftmost =  None
            while cur:
                # 此处的cur 节点表示当前层的节点
                prev,leftmost = self.connectChild(cur.left,prev,leftmost)
                prev,leftmost = self.connectChild(cur.right,prev,leftmost)
                cur = cur.next
        return root

    def connectChild(self,cur,prev,leftmost):
        # 此处的 cur 节点为下一层的节点
        if cur:
            if not prev:
                # 若 prev 为None，则当前遇到的 cur 为第一个节点，将 leftmost 赋值
                leftmost = cur
            else:
                # prev 不为 None，表示可以进行连接
                prev.next = cur
            # 更新 prev
            prev = cur
        return prev,leftmost
