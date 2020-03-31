#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-29 20:05:44
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def multiply(self, num1, num2):
        if not num1 or not num2:
            return ""
        if num1 == '0' or num2 == '0':
            return "0"

        last_pos = 0
        ans = ""
        for dig2 in num2[::-1]:
            print(ans)
            tem_mul = self.single_mul(num1,dig2)
            if last_pos < 0:
                ans = self.single_add(ans[:last_pos],tem_mul) + ans[last_pos:]
            else:
                ans = tem_mul
            last_pos -= 1
        return ans

            
    def single_add(self,num1,num2):
        num1 = num1[::-1]
        num2 = num2[::-1]
        pos = 0
        carrier = 0

        ans = ""
        while pos < max(len(num1),len(num2)):

            if pos < len(num1) and pos < len(num2):
                tem = int(num1[pos]) + int(num2[pos])
            elif len(num1) <= pos < len(num2):
                tem = int(num2[pos])
            elif len(num2) <= pos < len(num1):
                tem = int(num1[pos])
            if carrier > 0:
                tem += carrier
                carrier = 0

            if tem >= 10:
                carrier = tem//10
            tem %= 10
            ans += str(tem)
            pos += 1

        if carrier > 0:
            ans += str(carrier)
        return ans[::-1]

    def single_mul(self,num1,num):
        carrier = 0
        ans = ""
        num = int(num)
        for i in range(len(num1)-1,-1,-1):
            tem = num * int(num1[i])
            if carrier > 0:
                tem += carrier
                carrier = 0
            carrier = tem // 10
            tem = tem %10
            ans += str(tem)
        if carrier != 0:
            ans += str(carrier)
        return ans[::-1]

s = Solution()
print(s.multiply("123","456"))