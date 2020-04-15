#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-13 10:18:26
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # 使用 BFS，每一层的节点表示删除一个括号得到的结果

        def check(string):
            count = 0

            for c in string:
                if c == '(':
                    count += 1
                elif c == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        level = {s}
        while 1:
            valid = list(filter(check,level))
            if valid:
                return valid
            level = {string[:i] + string[i+1:] for string in level for i in range(len(string)) if string[i] in "()"}

s = Solution()
print(s.removeInvalidParentheses("()())()"))


