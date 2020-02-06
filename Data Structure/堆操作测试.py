#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-23 09:22:41
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
	def __init__(self):
		self.max_heap_list =[9999]
		self.min_heap_list = [-9999]

	def Insert(self,num):
		if (len(self.max_heap_list) + len(self.min_heap_list) - 1) %2 == 0:
			self.min_heap_list = self.InsertMinHeap(num)
			top_min = self.DeleteMinHeap()
			self.max_heap_list = self.InsertMaxHeap(top_min)
		else:
			self.max_heap_list = self.InsertMaxHeap(num)
			top_max = self.DeleteMaxHeap()
			self.min_heap_list = self.InsertMinHeap(top_max)

	def GetMedian(self):
		if len(self.min_heap_list) + len(self.max_heap_list) - 2 == 0 :
			return None
		if (len(self.min_heap_list) + len(self.max_heap_list)) %2 == 0:
			return float((self.max_heap_list[1] + self.min_heap_list[1])/2)
		else:
			return self.min_heap_list[1]

	def InsertMaxHeap(self,data):
		self.max_heap_list.append(data)
		start = len(self.max_heap_list) - 1
		while start > 1:
			cur_father = int(start/2)
			if self.max_heap_list[start] < self.max_heap_list[cur_father]:
				break
			elif self.max_heap_list[start] > self.max_heap_list[cur_father]:
				tem = self.max_heap_list[cur_father]
				self.max_heap_list[cur_father] = self.max_heap_list[start]
				self.max_heap_list[start] = tem
				start = cur_father
		return self.max_heap_list

	def DeleteMaxHeap(self):
		delete = self.max_heap_list[1]
		self.max_heap_list[1] = self.max_heap_list[-1]
		self.max_heap_list.pop()

		start = 1
		while start * 2 < len(self.max_heap_list):
			big_son = start * 2
			if big_son + 1 < len(self.max_heap_list):
				if self.max_heap_list[big_son + 1] > self.max_heap_list[big_son]:
					big_son = big_son + 1
			if self.max_heap_list[start] > self.max_heap_list[big_son]:
				break
			elif self.max_heap_list[start] < self.max_heap_list[big_son]:
				tem = self.max_heap_list[big_son]
				self.max_heap_list[big_son] = self.max_heap_list[start]
				self.max_heap_list[start] = tem
				start = big_son
		return delete

	def InsertMinHeap(self,data):
		self.min_heap_list.append(data)
		start = len(self.min_heap_list) - 1
		while start > 1:
			cur_father = int(start/2)
			if self.min_heap_list[start] > self.min_heap_list[cur_father]:
				break
			elif self.min_heap_list[start] < self.min_heap_list[cur_father]:
				tem = self.min_heap_list[cur_father]
				self.min_heap_list[cur_father] = self.min_heap_list[start]
				self.min_heap_list[start] = tem
				start = cur_father

		return self.min_heap_list

	def DeleteMinHeap(self):
		delete = self.min_heap_list[1]
		self.min_heap_list[1] = self.min_heap_list[-1]
		self.min_heap_list.pop()
		start = 1
		while start * 2 < len(self.min_heap_list):
			small_son = start * 2
			if small_son + 1 < len(self.min_heap_list):
				if self.min_heap_list[small_son + 1] < self.min_heap_list[small_son]:
					small_son = small_son + 1
			if self.min_heap_list[start] < self.min_heap_list[small_son]:
				break
			elif self.min_heap_list[start] > self.min_heap_list[small_son]:
				tem = self.min_heap_list[small_son]
				self.min_heap_list[small_son] = self.min_heap_list[start]
				self.min_heap_list[start] = tem
				start = small_son
		return delete


# 5,2,3,4,1,6,7,0,8
s = Solution()
s.Insert(5)
print(s.GetMedian())
# print(s.min_heap_list)
# print(s.max_heap_list)
s.Insert(2)
print(s.GetMedian())
# print(s.min_heap_list)
# print(s.max_heap_list)
s.Insert(3)
print(s.GetMedian())
# print(s.min_heap_list)
# print(s.max_heap_list)
s.Insert(4)
print(s.GetMedian())
# print(s.min_heap_list)
# print(s.max_heap_list)
s.Insert(1)
print(s.GetMedian())
# print(s.min_heap_list)
# print(s.max_heap_list)
s.Insert(6)
print(s.GetMedian())
# print(s.min_heap_list)
# print(s.max_heap_list)
s.Insert(7)
print(s.GetMedian())
# print(s.min_heap_list)
# print(s.max_heap_list)
s.Insert(0)
print(s.GetMedian())
# print(s.min_heap_list)
# print(s.max_heap_list)
s.Insert(8)
print(s.GetMedian())
# print(s.min_heap_list)
# print(s.max_heap_list)


# a = heap([79,66,43,83,30,87,38,55,91,72,49,9])
# print(a.max_heap_list)
# print(a.CreateMaxHeap())
# print(a.DeleteMaxHeap())
# print(a.max_heap_list)





