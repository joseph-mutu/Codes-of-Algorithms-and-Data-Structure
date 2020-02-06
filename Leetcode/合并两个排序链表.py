#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-03 11:21:32
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution():
	def mergeTwoLists(self, l1, l2):
		head = ListNode(-1)
		head_guard = head
		while l1 and l2:
			if l1.val < l2.val:
				head.next = l1
				l1 = l1.next
			else:
				head.next = l2
				l2 = l2.next
			head = head.next
		head.next = l1 if l1 else l2

		return head_guard.next
l1 = ListNode(1)
node1_l1 = ListNode(2)
l1.next = node1_l1
node2_l1 = ListNode(3)
node1_l1.next = node2_l1
l2 = ListNode(1)
node1_l2 = ListNode(2)
l2.next = node1_l2

s = Solution()
tem_head = s.mergeTwoLists(l1,l2)
while tem_head:
	print(tem_head.val)
	tem_head = tem_head.next


