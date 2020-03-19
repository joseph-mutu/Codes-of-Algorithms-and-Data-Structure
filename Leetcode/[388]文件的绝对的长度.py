#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-19 07:29:51
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    # 使用栈进行求解
    def lengthLongestPath(self, input):
        if '.' not in input:
            return 0
        input = input.split('\n')
        depth_file = []
        for tem in input:
            depth = tem.count('\t')
            # 消除括号，只保留文件名
            depth_file.append([depth,tem[depth:]])

        print(depth_file)
        def cal_len(stack):
            length = 0
            for i in stack:
                # +1 means plus '/'
                length += len(i[1]) +1
            return length - 1

        # stack is to store the path with asceding \t from bottom to top
        stack = []
        max_length = 0
        for tem in depth_file:
            while stack and tem[0] <= stack[-1][0]:
                stack.pop()
            stack.append(tem)
            # if the current string contains '.', it means we reach the bottom of one path
            if '.' in tem[1]:
                max_length = max(max_length,cal_len(stack))
        return max_length

s = Solution()
print(s.lengthLongestPath("dir\n    file.txt"))



