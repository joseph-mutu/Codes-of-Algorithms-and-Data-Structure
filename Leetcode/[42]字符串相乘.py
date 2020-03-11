#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-10 15:50:39
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if not num1 and not num2:
            return ""
        elif not num1:
            return num2
        elif not num2:
            return num1
        elif num1 == '0' or num2 == '0':
            return '0'
        ans_string = ""
        last_pos = 0
        for dig1 in num1[::-1]:
            cur_mul = self.single_mul(dig1,num2)
            if last_pos < 0:
                ans_string = self.sum_num(ans_string[:last_pos],cur_mul) + ans_string[last_pos:]
            else:
                ans_string = cur_mul
            last_pos -= 1
        return ans_string

    def sum_num(self,num1,num2):
        string_sum = ""
        pos = 0
        carrier = 0
        num1 = num1[::-1]
        num2 = num2[::-1]
        while pos < max(len(num1),len(num2)):
            if pos < len(num1) and pos < len(num2):
                cur_num = int(num1[pos]) + int(num2[pos])
            elif pos < len(num1) and pos >= len(num2):
                cur_num = int(num1[pos])
            elif pos >= len(num1) and pos < len(num2):
                cur_num = int(num2[pos])
            if carrier > 0:
                cur_num += carrier
                carrier = 0
            carrier = cur_num //10 
            cur_num %= 10
            string_sum += str(cur_num)
            pos += 1
        if carrier > 0:
            string_sum += str(carrier)
        return string_sum[::-1]


    def single_mul(self,num1,num2):
        num_string = ""
        num1 = int(num1)
        carrier = 0
        for num in num2[::-1]:
            num = int(num)
            cur_num = num1 * int(num)
            if carrier > 0:
                cur_num += carrier
                carrier = 0
            carrier = cur_num // 10
            cur_num %= 10
            num_string += str(cur_num)
        if carrier > 0:
            num_string += str(carrier)
        return num_string[::-1]