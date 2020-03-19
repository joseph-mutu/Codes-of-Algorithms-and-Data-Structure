#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-19 08:27:16
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os


class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        if '.' not in input:
            return 0
        max_len = 0
        depth_dic = {0:0}
        # depth_dic[depth + 1] 储存了 到 depth 为止的长度
        input = input.split('\n')
        for string in input:
            depth = string.count('\t')
            string = string.lstrip('\t')
            if '.' in string:
                max_len = max(max_len,depth_dic[depth] + len(string))
            depth_dic[depth + 1] = depth_dic[depth] + len(string) + 1
        return max_len