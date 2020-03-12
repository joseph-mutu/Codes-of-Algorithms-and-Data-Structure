#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-12 08:30:45
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        
        first_half = self.find_half_link(head)
        first_half_reverse = self.reverse(first_half.next)
        # 此时前一半链表与后一半链表断开

        is_reverse = True
        first_half_reverse_record = first_half_reverse
        head_record = head
        while is_reverse and first_half_reverse is not None:
            if head.val != first_half_reverse.val:
                is_reverse = False
            head = head.next
            first_half_reverse = first_half_reverse.next
        first_half.next = self.reverse(first_half_reverse_record)
        self.print_list(head_record)
        return is_reverse

    
    def find_half_link(self,head):
        # 使用快慢指针遍历链表寻找中间链表节点
        slow = head
        fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def reverse(self,head):
        if not head or not head.next:
            return head
        right = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return right
    def print_list(self,head):
        while head:
            print(head.val)
            head = head.next

head = ListNode(1)
node1 = ListNode(2)
node2 = ListNode(1)
node3 = ListNode(1)
# node4 = ListNode(5)
head.next = node1
node1.next = node2
node2.next = node3
# node3.next = node4

s = Solution()
print(s.isPalindrome(head))