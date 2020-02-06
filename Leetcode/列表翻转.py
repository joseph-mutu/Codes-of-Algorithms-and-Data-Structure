#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-02 21:15:19
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution():
	def reverseList(self, head):
		if not head:
			return None
		left = head
		right = head.next
		
		left.next = None
		while right:
			tem = right.next
			right.next = left
			left = right
			right = tem
		return left

head = ListNode(1)
node1 = ListNode(2)
node2 = ListNode(3)
node3 = ListNode(4)
node4 = ListNode(5)
head.next = node1
node1.next = node2
node2.next = node3
node3.next = node4


s = Solution()
print(s.reverseList(head).next.val)

