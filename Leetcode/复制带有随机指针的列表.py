#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-02 07:42:38
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

# Definition for a Node.
class Node:
	def __init__(self, x, next=None, random=None):
		self.val = int(x)
		self.next = next
		self.random = random

class Solution():
	def copyRandomList(self, head):
		"""
		:type head: Node
		:rtype: Node
		"""
		if not head:
			return None
		newhead = Node(-1)

		new_cur = newhead
		cur = head

		pointer_store = {}

		while cur:
			tem_node = Node(cur.val)
			pointer_store[cur] = tem_node
			new_cur.next = tem_node

			new_cur = new_cur.next
			cur = cur.next

		cur = head
		new_cur = newhead.next

		while cur:
			if cur.random is not None:
				new_cur.random = pointer_store[cur.random]
			cur = cur.next
			new_cur = new_cur.next

		return newhead.next




s = Solution()
head = Node(1)

print(s.copyRandomList(head))




	