#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-01-14 14:46:17
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class ListNode():
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution():

	def addTwoNumbers(self,l1,l2):

		head = ListNode(-1)
		ans = head
		carry = 0

		while l1 or l2:

			val1 = l1.val if l1 is not None else 0
			val2 = l2.val if l2 is not None else 0
			cur_val = val1 + val2 + carry
			
			ans.next = ListNode(cur_val%10)
			carry = int(cur_val/10)

			ans = ans.next
			if l1: l1 = l1.next
			if l2: l2 = l2.next

		if carry > 0:
			ans.next = ListNode(carry)

		return head.next

x = ListNode(2)
x.next = ListNode(4)
x.next.next = ListNode(3)

y = ListNode(5)
y.next = ListNode(6)
# y.next.next = ListNode(4)
s = Solution()
tem = s.addTwoNumbers(x,y)
print(tem.val)
print(tem.next.val)
print(tem.next.next.val)