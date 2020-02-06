#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-30 08:52:48
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
import numpy as np

class Sort():
	# def QuickSortInput(self,data):


	def QuickSort(self,data,left,right):
		if right - left > 10:
			pivot = self.Median3(data,left,right)
			left_poi = left
			right_poi = right
			while 1:
				while data[left_poi] < data[pivot]:
					left_poi += 1
				while data[right_poi] > data[pivot]:
					right_poi -= 1
				if right_poi - left_poi > 0:
					data = self.Swap(data,left_poi,right_poi)
				else:
					break 
			data = self.Swap(data,right-1,left_poi)
			data = self.QuickSort(data,left,left_poi-1)
			data = self.QuickSort(data,left_poi + 1,right)

		else:
			data = self.InsertSort(data,left,right)
		return data


	def Median3(self,data,left,right):
		# 选取主元
		center = int((left+right)/2)
		# 将 left cetner right 按照从小到大的顺序排好序
		if data[left] > data[center]:
			data = self.Swap(data,center,left)
		if data[center] > data[right]:
			data = self.Swap(data,center,right)
		if data[left] > data[center]:
			data = self.Swap(data,left,center)
		data = self.Swap(data,center,right-1)
		return data[right-1]


	def Swap(self,data,pos1,pos2):
		tem = data[pos1]
		data[pos1] = data[pos2]
		data[pos2] = tem

		return data

	def InsertSort(self,data,left,right):
		for i in range(left,right+1):
			cur_data = data[i]
			tem_pos = i - 1
			while tem_pos >= 0:
				if data[tem_pos] > cur_data:
					data[tem_pos+1] = data[tem_pos]
					tem_pos -= 1
				else:
					break
			data[tem_pos+1] = cur_data
		return data

data = np.arange(100)
np.random.shuffle(data)
print(data)
s = Sort()
print(s.QuickSort(data,0,len(data)-1))
