#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-15 12:42:33
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        circles = 0
        union = [-1] * len(M)
        for i in range(len(M)):
            for j in range(len(M)):
                if M[i][j] == 1 and i != j:

                    father_i = self.find_father(union,i)
                    father_j = self.find_father(union,j)
                    print(i,father_i,j,father_j)
                    if father_i != father_j:
                        if union[father_i] <= union[father_j]:
                            # father i has more children
                            union[father_i] += union[father_j]
                            union[father_j] = father_i
                            union[j] = father_i
                        else:
                            # father j has more children
                            union[father_j] += union[father_i]
                            union[father_i] = father_j
                            union[i] = father_j
        for i in union:
            if i < 0:
                circles += 1
        return circles


    def find_father(self,union,index):
        while union[index] >= 0:
            index = union[index]
        return index

s = Solution()
M = [
 [1,1,0],
 [1,1,1],
 [0,1,1]]
print(s.findCircleNum(M))