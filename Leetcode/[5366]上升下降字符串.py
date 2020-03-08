#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-07 15:34:00
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def sortString(self, s):
        """
        从 s 中选出 最小 的字符，将它 接在 结果字符串的后面。
        从 s 剩余字符中选出 最小 的字符，且该字符比上一个添加的字符大，
        将它 接在 结果字符串后面。

        重复步骤 2 ，直到你没法从 s 中选择字符。
        从 s 中选出 最大 的字符，将它 接在 结果字符串的后面。
        从 s 剩余字符中选出 最大 的字符，且该字符比上一个添加的字符小，
        将它 接在 结果字符串后面。
        重复步骤 5 ，直到你没法从 s 中选择字符。
        """
        if not s:
            return ""
        s = sorted(s)

        res = []
        while s:
            res.append(s[0])
            s.remove(s[0])
            remove_list = []
            for i in range(len(s)):
                if s[i] > res[-1]:
                    res.append(s[i])
                    remove_list.append(s[i])
            for x in remove_list:
                s.remove(x)
            remove_list = []
            if not s:
                break
            res.append(s[-1])
            s.remove(s[-1])

            for i in range(len(s)-1,-1,-1):
                if s[i] < res[-1]:
                    res.append(s[i])
                    remove_list.append(s[i])
            for x in remove_list:
                s.remove(x)
        return "".join(res)

s = Solution()
print(s.sortString(""))

