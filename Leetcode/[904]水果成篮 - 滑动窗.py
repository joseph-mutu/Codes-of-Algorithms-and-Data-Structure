#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-20 20:21:05
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$


import collections
class Solution(object):
    def totalFruit(self, tree):
        # 使用滑动窗口
        l,r = 0,0
        max_len = float('-inf')
        
        contain = collections.Counter()

        while r < len(tree):
            # move r to find a feasible solution
            # r 指向可行解末尾的下一位`
            contain[tree[r]] += 1
            if len(contain) <= 2:
                if r - l + 1 > max_len:
                    max_len = r - l + 1

            # 缩小左边界
            while len(contain) > 2:
                contain[tree[l]] -= 1
                if contain[tree[l]] == 0:
                    del contain[tree[l]]
                l += 1
            r += 1
        return max_len
s = Solution()
print(s.totalFruit([]))



        
        
