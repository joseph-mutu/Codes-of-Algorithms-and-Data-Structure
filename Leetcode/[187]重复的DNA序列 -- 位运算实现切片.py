#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-02 06:29:45
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        if not s or len(s) < 10:
            return []
        #使用位运算实现切片

        to_int = {'A':0,'C':1,'G':2,'T':3}
        nums = [to_int[i] for i in s]

        L,n = 10,len(s)
        #滑动窗口
        l =0

        bitmask = 0
        # 计算初始 L长度序列的 bitmask 

        results = set()
        record = set()

        while l < n - L +1:
        # for l in range(n - L + 1):
            if l == 0:
                # 检查初始序列
                for i in range(L):
                    # 先将 bitmask 左移两位，腾出最后的空间
                    bitmask <<= 2
                    bitmask |= nums[i]
            else:
                #左移腾出第1,2位
                bitmask <<= 2
                #将最后两位置为 0
                bitmask &= ~(3 << 2*L)

                #添加当前位置
                bitmask |= nums[l + L - 1]
            #检查
            if bitmask in record:
                results.add(s[l:l+L])
            else:
                record.add(bitmask)
            l += 1
        return list(results)

s = Solution()
print(s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))