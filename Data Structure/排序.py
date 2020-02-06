#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-08 08:45:41
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
import numpy as np

def swap(data,pos1,pos2):
	tem = data[pos1]
	data[pos1] = data[pos2]
	data[pos2] = tem
	return data

def adjust_heap(data,start_node,number_data):
	while 1:
		child_left = 2*start_node + 1
		child_right = 2*start_node + 2
		if child_right > number_data-1:
			if child_left > number_data-1:
				break
			elif data[child_left] > data[start_node]:
				data = swap(data,start_node,child_left)
				break
			else:
				break
		elif data[start_node] >= max(data[child_left],data[child_right]):
			break
		if data[child_left] > data[child_right]:
			if data[start_node] < data[child_left]:
				data = swap(data,start_node,child_left)
				start_node = child_left
		elif data[child_left] < data[child_right]:
			if data[start_node] < data[child_right]:
				data = swap(data,start_node,child_right)
				start_node = child_right
	return data

def max_heap(data):
	#找到完全二叉树中最后一个节点的父节点
	if (len(data)-1)%2 ==0:
		first_node = int((len(data)-3)/2)
		first_left = 2*first_node + 1
		first_right = 2*first_node + 2
		if data[first_left] > data[first_node]:
			data = swap(data,first_left,first_node)
		if data[first_right] > data[first_node]:
			data = swap(data,first_right,first_node)
	elif (len(data)-1)%2  == 1:
		first_node = int((len(data)-2)/2)
		first_left = 2*first_node + 1
		if data[first_left] > data[first_node]:
			data = swap(data,first_left,first_node)

	#对最后一个有儿子的节点进行处理，因为它要判断是否存在右儿子

	for i in range(first_node-1,-1,-1):
		data = adjust_heap(data,i,len(data))
	return data

def heap_sort(data,number):
	number -= 1
	data = max_heap(data)
	data = swap(data,0,number)
	for i in range(number-1,-1,-1):
		data = adjust_heap(data,0,number)
		number -= 1
		data = swap(data,0,number)
	return data
def bubble_sort(number,data):
	flag = False
	for p in range(number,-1,-1):
		for j in range(p-1):
			if data[j] > data[j+1]:
				swap(data,j,j+1)
				flag = True
		if flag == False:
			break

def insert_sort(number,data):
	for p in range(1,number):
		tem = data[p]
		for i in range(p,-1,-1):
			if data[i-1] > tem and i > 0:
				data[i] = data[i-1]
			else:
				break
		data[i] = tem
	return data

def shell_sort(number,data):
	sedgewick = [1,5,19,41,109]
	for sed in range(len(sedgewick)-1,-1,-1):
		inc = sedgewick[sed]
		if inc-1 > len(data):
			continue
		else:
			for i in range(inc,len(data),inc):
				tem = data[i]
				for j in range(i,-1,-inc):
					if data[j-inc] > tem and j > 0:
						data[j] = data[j-inc]
					else:
						break
				data[j] = tem
	return data

#以下为归并排序

def merge(data,real_order,start1,start2,end,length):
	bound1 = start1 + length
	cur_count = start1
	while 1:
		if start1 >= bound1 or start2 >= end:
			break
		if data[start1] > data[start2]:
			real_order[cur_count] = data[start2]
			start2 += 1
			cur_count += 1

		elif data[start1] < data[start2]:
			real_order[cur_count] = data[start1]
			start1 += 1
			cur_count += 1

	if start1 >= bound1:
		while start2 < end:
			real_order[cur_count] = data[start2]
			start2 += 1
			cur_count += 1
	elif start2 >= end:
		while start1 < bound1:
			real_order[cur_count] = data[start1]
			start1 += 1
			cur_count += 1
	return real_order
 

def merge_sort(data,real_order):
	length = 1
	while length < len(data):
		i = 0
		pairs = int(len(data)/(2*length))

		# 2*length*pairs 表示从最后开始，把最后两个子列单独考虑
		while i < 2*length*pairs:
			real_order = merge(data,real_order,i,i+length,i+2*length,length)
			i += 2*length
		
		if  i + length < len(data):
			# 说明数据在当前长度的分割下，最后还剩下两个子列
			# 注意对于当前长度为 1 的序列，我们要进行 2 * 1 序列的比对
			# 对于长度为 2 的序列，我们要进行 2 * 2 长度序列的比对
			real_order = merge(data,real_order,i,i+length,len(data),length)

		elif i + length >= len(data):
			while i < len(data):
				real_order[i] = data[i]
				i += 1
		for i in range(len(data)):
			data[i] = real_order[i]
		length *= 2
	return real_order


number = int(input())
data = list(map(int,input().split()))
data = merge_sort(number,data)
print(" ".join(str(i) for i in data ))
