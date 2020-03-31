#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-30 07:47:20
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
s
import collections
class Solution(object):
    def subarraySum(self, nums, k):
        # 前缀和
        if not nums:
            return 0
        
        # 建立前缀和数组
        pre_sum = collections.Counter()
        pre_sum[0] += 1
        
        count = 0
        tem_sum = 0
        for num in nums:
            tem_sum += num
            target = tem_sum - k
            if pre_sum[target] > 0:
                count += pre_sum[target]
            pre_sum[tem_sum] += 1
        return count
s = Solution()
print(s.subarraySum([1,2,3],3))