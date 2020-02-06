#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-03 09:10:00
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution():
	def reverseList(self, head):
		if not head or not head.next:
			return head
		right = self.reverseList(head.next)
		head.next.next = head
		head.next = None
		return right