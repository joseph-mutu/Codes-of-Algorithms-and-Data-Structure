#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-08 18:51:21
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
    def reverseKGroup(self, head, k):
        if not head or head.next is None:
            return head

        new_head, old_head = self.reverseK(head,k)
        record = new_head

        while 1:
            tem_new,tem_old = self.reverseK(old_head.next,k)

            if tem_new is None:
                old_head.next = tem_old
                break
            old_head.next = tem_new
            old_head = tem_old

        return record
        
    def reverseK(self,head,k):
        if not head:
            return (None,head)
        # detect if the length is enough
        if not self.detecter(head,k):
            return (None,head)
        record = head
        l,r = head,head.next

        for i in range(k-1):
            tem = r.next
            r.next = l
            l = r
            r = tem
        record.next = r
        return (l,record)
    
    def detecter(self,head,k):
        count = 0
        while head:
            count += 1
            head = head.next
            if count >= k:
                return True
        return False


head = ListNode(1)
head.next = ListNode(2)
head.next.next  = ListNode(3)
head.next.next.next = ListNode(4)

s = Solution()
new_head = s.reverseKGroup(head,3)
print(new_head.next.next.next.next)
# tem1,tem2 = s.reverseK(head,2)