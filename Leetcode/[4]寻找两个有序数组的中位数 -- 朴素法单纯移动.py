#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-09 07:27:38
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        len1 = len(nums1)
        len2 = len(nums2)

        length = len1 + len2

        p1,p2 = 0,0
        l,r = -1,-1

        median = 0

        for i in range((length // 2)+ 1):
            l = r
            if p1 < len1 and (p2 >= len2 or nums1[p1] < nums2[p2]):
                r = nums1[p1]
                p1 += 1
            else:
                r = nums2[p2]
                p2 += 1
        if length & 1 == 1:
            # if the total length is odd
            median = r/1.0
            
        else:
            median = (l+r)/2.0
        return median
    
