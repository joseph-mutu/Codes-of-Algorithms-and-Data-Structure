#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-22 07:20:17
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        guard = ListNode(-1)
        guard.next = head
        pre = guard

        while head and head.next:

            first = head
            second = head.next

            # swap the node
            pre.next = second
            first.next = second.next
            second.next = first

            #update pre and head
            pre = first
            head = first.next

        return guard.next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

s = Solution()
new_heade = s.swapPairs(head)
while new_heade:
    print(new_heade.val)
    new_heade = new_heade.next





