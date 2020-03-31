#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-30 09:16:43
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class SegmentNode:
    def __init__(self,start,end,val,left = None,right = None):
        #attributes
        self.start = start
        self.end = end
        self.val = val
        # children
        self.left = left
        self.right = right

class NumArray:

    def __init__(self, nums):
        if not nums or nums is None:
            return None
        self.root = self.build(0,len(nums)-1,nums)

    def build(self,start,end,nums):
        # T(n) = 2*T(n/2) = O(n)
        if start == end:
            return SegmentNode(start,end,nums[start])

        mid = (start + end)//2

        left = self.build(start,mid,nums)
        right = self.build(mid+1,end,nums)

        return SegmentNode(start,end,left.val + right.val,left,right)

    def update(self, i, val):

        def update_seg(root,i,val):
            if root.start == i and root.end == i:
                root.val = val
                return 
            mid = (root.start + root.end)//2
            if i <= mid:
                update_seg(root.left,i,val)
            else:
                update_seg(root.right,i,val)

            root.val = root.left.val + root.right.val
        update_seg(self.root,i,val)        

    def sumRange(self, i, j):
        def sumRange_seg(root,i,j):
            if root.start == i and root.end == j:
                return root.val
            mid = (root.start + root.end)//2

            if j <= mid:
                return sumRange_seg(root.left,i,j)
            elif i > mid:
                return sumRange_seg(root.right,i,j)
            else:
                return sumRange_seg(root.left,i,mid) + sumRange_seg(root.right,mid+1,j)
        return sumRange_seg(self.root,i,j)

s = NumArray(None)
s.update(1,2)
print(s.root.val)








