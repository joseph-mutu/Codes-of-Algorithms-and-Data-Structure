#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-02 10:23:25
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Node:
	def __init__(self, x, next=None, random=None):
		self.val = int(x)
		self.next = next
		self.random = random

class Solution():
	def copyRandomList(self, head):
		if not head:
			return None

		cur = head
		while cur:
			tem_node = Node(cur.val)
			tem_next = cur.next
			cur.next = tem_node
			tem_node.next = tem_next
			cur = tem_node.next

		cur = head
		while cur:
			if cur.random is not None:
				cur.next.random = cur.random.next
			cur = cur.next
			if cur.next is None:
				break
			cur = cur.next
		cur = head

		new_head = head.next

		cur = head
		while cur.next:
			tem_next = cur.next
			cur.next = tem_next.next
			cur = tem_next
		cur.next = None
		return new_head

Node1 = Node(1)
Node2 = Node(2)
Node3 = Node(3)
Node1.next = Node2
Node1.random = None
Node2.next = Node3
Node2.random = Node1
Node3.random = Node1
head = Node1

s = Solution()
print(s.copyRandomList(head))