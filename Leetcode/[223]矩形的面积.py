#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-13 16:58:29
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        rec_points = [[(A,B),(C,D)],[(E,F),(G,H)]]
        return self.is_covered(rec_points)

    # def covered_area(self,rec_points):
    
    def is_covered(self,rec_points):
        rec1_A = rec_points[0][0]
        rec1_B = rec_points[0][1]
        
        rec2_A = rec_points[1][0]
        rec2_B = rec_points[1][1]

        # right
        if rec1_A[0] <= rec2_A[0] >= rec2_A[0] and rec1_B[0] <= rec2_A[0] >= rec2_B[0]:
            return False
        # up
        elif rec1_A[1] <= rec2_A[1] >= rec1_B[1] and rec1_A[1] <= rec2_B[1] >= rec1_B[1]:
            return False  
        # left
        elif rec1_A[0] >= rec2_A[0] <= rec1_B[0] and rec1_A[0] >= rec2_B[0] <= rec1_B[0]:
            return False
        # down
        elif rec1_A[1] >= rec2_A[1] <= rec1_B[1] and rec1_A[1] >= rec2_B[1] <= rec1_B[1]:
            return False
        return True
s = Solution()
print(s.computeArea(-3,-3,-1,-1,3,-3,0,0))
