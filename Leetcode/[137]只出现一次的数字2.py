#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-27 07:04:00
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def singleNumber(self, nums):
        ans = 0
        # 表示当前对 32 位整型进行处理
        for i in range(32):
            count = 0
            #第一位为符号位，所以不对32位进行操作
            for num in nums:
                # 表示第 i 位 为1
                if (num >> i & 1) == 1:
                    count += 1

            if count % 3 != 0:
                ans |= 1 << i
        return ans if not (ans >> 31 & 1) else -((~ans +1) & 0xffffffff)

s = Solution()
print(s.singleNumber([-2,-2,1,1,-3,1,-3,-3,-4,-2]))