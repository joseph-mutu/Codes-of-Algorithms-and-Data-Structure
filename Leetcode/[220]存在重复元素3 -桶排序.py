#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-31 10:38:53
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if not nums or t <0:
            return False
        buckets = {}
        size = t + 1

        for idx,val in enumerate(nums):
            bucket_num = val // size
            print(idx,val,bucket_num,buckets)
            if idx > k:
                print(idx)
                if buckets.get(nums[idx-k-1]//size) is not None:
                    del buckets[nums[idx - k - 1]//size]
            
            
            if buckets.get(bucket_num) is not None:
                return True
            #检查左右两边的桶
            if buckets.get(bucket_num - 1) and abs(val - buckets[bucket_num-1]) <= t:
                return True
            elif buckets.get(bucket_num + 1) and abs(val - buckets[bucket_num + 1]) <= t:
                return True
            buckets[bucket_num] = val
            print(idx,val,bucket_num,buckets)
        return False

s = Solution()
print(s.containsNearbyAlmostDuplicate( nums = [1,2,3,1], k = 3, t = 0))