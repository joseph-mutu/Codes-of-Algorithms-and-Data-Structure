#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-28 06:50:06
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        想法:
            - 计算两个链表的长度
            - 移动长的链表使两个链表长度一致
            - 同时移动两个链表并进行比对
        """
        if not headA or not headB:
            return None

        # 计算 headA 的长度
        len_A = 0
        tem_headA = headA
        while tem_headA:
            len_A += 1
            tem_headA = tem_headA.next
        # 计算 headB 的长度
        len_B = 0
        tem_headB = headB
        while tem_headB:
            len_B += 1
            tem_headB = tem_headB.next
        # 使两个链表长度一致
        if len_A > len_B:
            while len_A != len_B:
                headA = headA.next
                len_A -= 1
        else:
            while len_A != len_B:
                headB = headB.next
                len_B -= 1
        # 同时移动两个链表，并进行比对
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

        return None