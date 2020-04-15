#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-13 19:10:23
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        l1_stack,l2_stack = [],[]

        h1 =l1
        while h1:
            l1_stack.append(h1.val)
            h1 = h1.next

        h2 = l2
        while h2:
            l2_stack.append(h2.val)
            h2 = h2.next

        res = 0
        cur_node,next_node = None,None
        while l1_stack or l2_stack:
            if l1_stack:
                res += l1_stack.pop()
            if l2_stack:
                res += l2_stack.pop()
            cur_node = ListNode(res%10)
            cur_node.next = next_node
            res //= 10
            next_node = cur_node
        if res:
            head = ListNode(res)
            head.next = next_node
            return head
        return cur_node





s = Solution()
head1 = ListNode(7)
head1.next = ListNode(2)
head1.next.next = ListNode(4)
head1.next.next.next = ListNode(3)


head2 = ListNode(5)
head2.next = ListNode(6)
head2.next.next = ListNode(4)
nhead = s.addTwoNumbers(head1,head2)
print(nhead.val)
print(nhead.next.val)
print(nhead.next.next.val)
print(nhead.next.next.next.val)



