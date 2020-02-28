#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-27 06:32:21
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stack1 = []
        stack2 = []

        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        res = ListNode(0)
        while stack1 or stack2:
            if stack1:
                res.val += stack1.pop()
            if stack2:
                res.val += stack2.pop()

            carrier = ListNode(res.val//10)
            res.val = res.val %10

            carrier.next = res

            res = carrier

        return res.next if res.val == 0 else res

s = Solution()
head_l1 = ListNode(7)
head_l1.next = ListNode(2)
head_l1.next.next = ListNode(4)
head_l1.next.next.next = ListNode(3)


head_l2 = ListNode(5)
head_l2.next = ListNode(6)
head_l2.next.next = ListNode(4)

head = s.addTwoNumbers(head_l1,head_l2)
while head:
    print(head.val)
    head = head.next