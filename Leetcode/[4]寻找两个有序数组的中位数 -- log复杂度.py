#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-09 07:28:09
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        len1 = len(nums1)
        len2 = len(nums2)

        length = len1 + len2
        l,r = (length + 1) //2,(length + 2)//2
        return (self.get_k(nums1,nums2,l) + self.get_k(nums1,nums2,r)) / 2.0
    
    def get_k(self,nums1,nums2,target):
        if not nums1:
            return nums2[target-1]
        if not nums2:
            return nums1[target-1]
        if target == 1:
            return nums1[0] if nums1[0] < nums2[0] else nums2[0]

        judge = target // 2

        pos1 = judge if judge < len(nums1) else len(nums1)
        pos2 = judge if judge < len(nums2) else len(nums2)

        if nums1[pos1-1] < nums2[pos2-1]:
            return self.get_k(nums1[pos1:],nums2,target - pos1)
        else:
            return self.get_k(nums1,nums2[pos2:],target - pos2)


s = Solution()
a = [1,3]
b = [2]
print(s.findMedianSortedArrays(a,b))