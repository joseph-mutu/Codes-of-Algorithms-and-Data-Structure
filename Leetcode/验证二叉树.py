#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-13 20:14:04
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.check(root)

    def check(self,node,lower_bound = float('-inf'), upper_bound = float('inf')):
        if node is None:
            return True

        cur_val = node.val

        if cur_val <= lower_bound or cur_val >= upper_bound:
            return False

        left_check = self.check(node.left,lower_bound,cur_val)
        right_check = self.check(node.right,cur_val,upper_bound)
        
        if not left_check:
            return False
        if not right_check:
            return False

        return True



