#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-18 21:24:49
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$


import collections
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False
        s_dic = collections.Counter(s)
        if_odd = 0
        for i in s_dic:
            
            if s_dic[i] & 1 == 1:
                if_odd += 1
        print(if_odd)
        if if_odd >1:
            return False
        return True
s = Solution()
print(s.canPermutePalindrome("aa"))