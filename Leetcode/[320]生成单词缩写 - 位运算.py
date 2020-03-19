#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-16 07:45:13
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os


class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        abb = []
        # 0 表示保留当前字符，1 意味着使用数字替代
        # 一共存在 2^n  个字符
        for x in range(1<<len(word)):
            # 0,1,2,3,4,每个数字代表一个状态
            # 1 的二进制为 0001, 1<<4 表示 1 0000 表示上限
            one_cnt = 0
            tem = ""
            for i in range(len(word)):
                # 判断末尾是否为 0
                if x & 1 == 0:
                    if one_cnt != 0:  
                        tem += str(one_cnt)
                        one_cnt = 0
                    tem += word[i]
                else:
                    one_cnt += 1
                # 判断 x 的下一位
                x=x>>1
            if one_cnt > 0:
                tem += str(one_cnt)
            abb.append(tem)
        return abb
        

s = Solution()
print(s.generateAbbreviations("word"))