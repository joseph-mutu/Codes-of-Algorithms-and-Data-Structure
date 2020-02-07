#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-07 06:28:39
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import re

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) & 1 == 1:
            return False

        # 判断是否存在非法的输入
        pa1 = r"[^\[\]\(\)\{\}]"
        pattern = re.compile(pa1)
        tem_pattern = pattern.findall(s)
        if tem_pattern:
            return False

        right_paren = [')',']','}']
        left_paren = ['(','[','{']
        paren_list = []
        for item in s:
            if item in left_paren:
                paren_list.append(item)
            elif item in right_paren:
                if not paren_list:
                    print(1)
                    return False
                tem_paren = paren_list.pop()
                if tem_paren != left_paren[right_paren.index(item)]:
                    print(1)
                    return False
        return not bool(paren_list)



s = Solution()
print(s.isValid('(('))