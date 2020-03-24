#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-22 13:29:32
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def nthUglyNumber(self, n):
        # min heap
        heap = [float('-inf'),1]

        ugly = []

        while len(ugly) < n:
            print(heap)
            node = self.get_item(heap)
            ugly.append(node)
            while ugly and node = ugly[-1]:
                ugly.append(node)
            self.add(heap,node*2)
            self.add(heap,node*3)
            self.add(heap,node*5)
            
        return ugly[n-1]

    def get_item(self,num):
        if len(num) == 2:
            return num.pop()
        tem = num[1]
        num[1] = num.pop()

        node = 1

        while node * 2 < len(num):
            child = node * 2
            # choose the smallest from two children
            if child + 1 < len(num) and num[child + 1] < num[child]:
                child += 1
            if num[child] < num[node]:
                num[node],num[child] = num[child],num[node]
            node = child 
        return tem

    def add(self,num,val):
        num.append(val)

        node = len(num) - 1 

        while num[node//2] > num[node]:
            parent = node//2
            if num[parent] > num[node]:
                num[node],num[parent] = num[parent],num[node]
            node = parent

s = Solution()
print(s.nthUglyNumber(1))


