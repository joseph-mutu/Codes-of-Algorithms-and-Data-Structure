#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-06 06:37:26
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os


# # The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        从第一个人开始遍历，假设名人为 0
        若当前名人不认识一个人，则更新名人为那个人
        这一步因为名人不认识任何人，所以遇到 0 进行更新
        如果真的遇到除自己以外全 0 的那一行，res 不会再进行更新
        """
        if n <= 0:
            return -1

        cle = 0
        for i in range(n):
            if knows(res,i):
                cle = i
        # 判断该 cle 是否为真的名人
        # 需要首先判断 cle 的前半段，因为不确定前半段是否所有人都认识该 cle and cle 不认识所有人
        # 在判断后半段，这是只需判断是否 所有人都认识该 cle 即可，因为可以保证该 cle 不认识后半段的所有人

        for i in range(cle):
            if knows(i,cle) and not knows(cle,i):
                continue
            return -1

        for i in range(cle+1,n):
            if knows(i,cle):
                continue
            return -1
        if not knows(cle,cle):
            return -1
        return cle
