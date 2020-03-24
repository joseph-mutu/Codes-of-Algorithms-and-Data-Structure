#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-21 16:17:17
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$


class Solution(object):
    def getKth(self, lo, hi, k):
        weights = []
        for i in range(lo,hi+1):
            weights.append([self.get_weight(i),i])
        weights = sorted(weights,key = lambda x:(x[0],x[1]))
        print(weights)
        return weights[k-1][1]

    def get_weight(self,num):
        steps = 0
        while num != 1:
            if num & 1 == 1:
                # 如果是奇数
                num = 3*num + 1
            else:
                num //= 2
            steps += 1
        return steps

s = Solution()
print(s.getKth(7,11,4))

            