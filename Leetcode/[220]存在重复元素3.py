#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-31 08:13:02
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if not nums:
            return False
        if nums and k == 0 and t > 0:
            return False
        elif nums and k == 0 and t == 0:
            return False

        # 维护一个长度为 k + 1 的滑动窗口，实时更新 min 和 max 的值
        #min and max stores the index
        window_min = [0]
        window_max = [0]

        for i in range(1,len(nums)):
            print(nums[i],window_min,window_max)
            if i - window_max[0] > k:
                window_max.pop(0)
            if i - window_min[0] > k:
                window_min.pop(0)

            if abs(nums[i] - nums[window_min[0]]) <= t or abs(nums[i] - nums[window_max[0]]) <= t:
                return True
            else:

                start = 0 if i - k < 0 else i-k

                for pos in range(start,i):
                    print(i)
                    if abs(nums[pos] - nums[i]) <= t:
                        return True
            #更新 window_max 以及 window_min
            while window_min and nums[i] <= window_min[-1]:
                window_min.pop()
            window_min.append(i)
            while window_max and nums[i] >= window_max[-1]:
                window_max.pop()
            window_max.append(i)
        return False

s = Solution()
print(s.containsNearbyAlmostDuplicate([0,1,2,3,4,1],5,0))




