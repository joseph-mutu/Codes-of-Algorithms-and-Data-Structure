#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-11 21:15:27
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        #如果当前节点为空，或者当前只有一个节点
        if not head or not head.next:
            return head

        mid_next = self.find_mid(head)
        left = self.sortList(head)
        right = self.sortList(mid_next)

        #merge
        guard = ListNode(0)
        merge_point = guard

        while left and right:
            if left.val > right.val:
                merge_point.next = right
                merge_point,right = merge_point.next,right.next
            else:
                merge_point.next = left
                merge_point,left = merge_point.next,left.next
        if left:
            merge_point.next = left
        if right:
            merge_point.next = right

        return guard.next

    def find_mid(self,head):
        slow,fast = head,head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid_next = slow.next
        slow.next = None
        #比如 1-> 2 -> 3 -> 4 -> None
        # mid = 4
        # slow = 3
        return mid_next

s = Solution()
head = ListNode(3)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
nhead = s.sortList(head)
print(nhead.val)
print(nhead.next.val)
print(nhead.next.next.val)
print(nhead.next.next.next.val)