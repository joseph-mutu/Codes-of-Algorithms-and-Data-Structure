#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-01 07:24:59
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def productExceptSelf(self, nums):
        if not nums:
            return []
        
        product_all = 1
        num_zeros = 0
        product_except_self = []

        for num in nums:
            if num:
                product_all *= num
            else:
                num_zeros += 1

        for num in nums:
            # 如果当前值为 0
            if not num:
                #若数组中不止 1 个0
                if num_zeros - 1 > 0:
                    product_except_self.append(0)
                else:
                # 若数组中只有一个0
                    product_except_self.append(product_all)
            # 若当前值不为 0 
            else:
                if num_zeros:
                    product_except_self.append(0)
                else:
                    product_except_self.append(product_all / num)
        return product_except_self

s = Solution()
print(s.productExceptSelf([0,1]))