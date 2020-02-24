#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-22 17:46:52
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        fast = head.next
        slow = head

        while fast and slow:
            if fast == slow:
                return True
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
            else:
                return False
        return False

head = ListNode(1)
head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = head

s = Solution()
print(s.hasCycle(head))