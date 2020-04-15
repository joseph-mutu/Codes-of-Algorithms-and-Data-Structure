#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-15 17:04:02
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None

        #first get the length of the linked list
        length = 0
        tem = head
        while tem:
            tem = tem.next
            length += 1
        k %= length
        if k == 0:
            return head
        else:
            # use two pointers as a ruler to find the last kth nodes
            k += 1
            l,r = head,head
            cur_len = 1
            while r.next:
                if cur_len != k:
                    r = r.next
                    cur_len += 1
                    continue
                l = l.next
                r = r.next
            #l points to the node that shhold be cut down
            record = l.next
            l.next = None
            r.next = head
            return record
                
s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)
n_head = s.rotateRight(head,4)
print(n_head.val)

