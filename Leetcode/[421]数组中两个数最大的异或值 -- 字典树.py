#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-04 08:44:20
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os


class Solution(object):
    def __init__(self):
        self.root = {}
        self.max_xor = 0
    def findMaximumXOR(self, nums):
        if not nums or len(nums) <= 1:
            return 0

        # convert numn into bit and zero-padding
        L = len(bin(max(nums))) - 2
        nums = [ [x>>i & 1 for i in range(L)][::-1] for x in nums]
        print(nums)
        self.insert_search(nums)

        return self.max_xor

    def insert_search(self,nums):

        for num in nums:
            node = self.root
            xor_node = self.root
            tem_xor = 0

            for bit in num:
                # insert the node
                if bit not in node:
                    node[bit] = {}
                node = node[bit]

                # compare the inserted node with others in the same layer
                target = 1 - bit
                if target in xor_node:
                    # 给最后一位腾出 0 并在最后一位+ 1
                    tem_xor = (tem_xor << 1) | 1
                    xor_node = xor_node[target]
                else:
                    tem_xor = tem_xor << 1
                    xor_node = xor_node[bit]
            self.max_xor = max(tem_xor,self.max_xor)

s = Solution()
print(s.findMaximumXOR([3, 10, 5, 25, 2, 8]))
        

