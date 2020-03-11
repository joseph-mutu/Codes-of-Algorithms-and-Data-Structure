#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-10 06:31:15
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
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return None
        guard = ListNode(-1)
        guard.next = head

        # build a ruler
        pre = guard
        left = head 
        right = head
        while n > 1:
            if right:
                right = right.next
            n -= 1

        if not right:
            # 说明 n 大于 链表长度
            return guard.next

        while right.next:
            pre = pre.next
            left = left.next
            right = right.next
        
        # #delete the node
        pre.next = left.next

        return guard.next

        
head = ListNode(1)
head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)

s = Solution()
head = s.removeNthFromEnd(head,1)
while head:
    print(head.val)
    head = head.next