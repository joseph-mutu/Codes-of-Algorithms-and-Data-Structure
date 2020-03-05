#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-05 14:45:42
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def removeKdigits(self, num, k):
        # 找到最小值

        num_stack = []

        for dig in num:
            # 从第二个数开始，如果当前数比栈中最后一个数小，则弹出栈中的元素
            while k and num_stack and num_stack[-1] > dig:
                num_stack.pop()
                k -= 1
            num_stack.append(dig)
        # 在极端的例子下，数字为增序，则删除后 K 个数字
        num_stack = num_stack[:-k] if k else num_stack
        return "".join(num_stack).lstrip('0') or '0'

s = Solution()
print(s.removeKdigits("10",1))
