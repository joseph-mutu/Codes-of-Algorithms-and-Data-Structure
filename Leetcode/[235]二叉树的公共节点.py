#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-28 06:50:41
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
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None
        if root == p or root == q:
            return root
        if (p.val < root.val and q.val > root.val) or (p.val > root.val and q.val < root.val ):
            LCS =  root
        # 若均在左边
        if p.val < root.val and q.val < root.val:
            LCS = self.lowestCommonAncestor(root.left,p,q)
        if p.val > root.val and q.val > root.val:
            LCS = self.lowestCommonAncestor(root.right,p,q)
        return LCS
