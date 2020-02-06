#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-06 21:11:38
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
import numpy as np

class node:
	def __init__(self, coe, exp):
		self.coe = coe
		self.exp = exp
		self.next = None
	def get_data(self):
		print(self.coe,self.exp)

class chain_list:
	def __init__(self):
		self.head = None
	def add_node(self,node):
		tem = self.head
		while tem.next is not None:
			tem = tem.next
		tem.next = node
	def print_node(self):
		tem = self.head
		while tem.next is not None:
			tem.get_data()
			tem = tem.next
		tem.get_data()


def add(l1,l2):
	ansl = []
	l1 = l1.head
	l2 = l2.head 
	if l1 is None and l2 is not None:
		while(l2 is not None):
			ansl.append([l2.coe,l2.exp])
			l2 = l2.next
		return ansl
	elif l2 is None and l1 is not None:
		while(l1 is not None):
			ansl.append([l1.coe,l1.exp])
			l1 = l1.next
		return ansl
	elif l2 is None and l1 is None:
		return [0,0]
	else:
		while(l1 is not None and l2 is not None):
			if l1.exp == l2.exp:
				tem_coe = l1.coe + l2.coe
				tem_exp = l1.exp
				l1 = l1.next
				l2 = l2.next
				if tem_coe != 0:
					ansl.append([tem_coe,tem_exp])
			elif l1.exp > l2.exp:
				tem_coe = l1.coe
				tem_exp = l1.exp
				if tem_coe != 0:
					ansl.append([tem_coe,tem_exp])
				l1 = l1.next
			elif l1.exp < l2.exp:
				tem_coe = l2.coe
				tem_exp = l2.exp
				if tem_coe != 0:
					ansl.append([tem_coe,tem_exp])
				l2 = l2.next
		if l1 is not None:
			while(l1 is not None):
				if l1.coe !=0:
					ansl.append([l1.coe,l1.exp])
				l1 = l1.next
			return ansl
		elif l2 is not None:
			while(l2 is not None):
				if l2.coe !=0:
					ansl.append([l2.coe,l2.exp])
				l2 = l2.next
			return ansl
		else:
			return ansl

def mul(l1,l2):
	l1 = l1.head
	l2 = l2.head
	coe = []
	exp = []
	ans = []
	if l1 is None or l2 is None:
		return [0,0]
	while l1 is not None:
		tem_l2 = l2
		while tem_l2 is not None:
			tem_coe = l1.coe * tem_l2.coe
			tem_exp = l1.exp + tem_l2.exp
			if tem_coe != 0:
				coe.append(tem_coe)
				exp.append(tem_exp)
			tem_l2 = tem_l2.next
		l1 = l1.next
	exp_unique = np.unique(exp)[::-1]
	num_exp_uni = len(exp_unique)
	for i in range(num_exp_uni):
		tem_coe = 0
		index = np.where(exp == exp_unique[i])[0]
		num_index = len(index)
		for j in range(num_index):
			tem_coe += coe[index[j]]
		if tem_coe != 0:
			ans.append(tem_coe)
			ans.append(exp_unique[i])
	return ans


#4 3 4 -5 2  6 1  -2 0
#3 5 20  -7 4  3 1
data1 = list(map(int,input().split()))
data2 = list(map(int,input().split()))

number_data1 = data1[0]
number_data2 = data2[0]
l1 = chain_list() 
l2 = chain_list()
if number_data1 > 0:
	count = 0
	tem_node = node(data1[count+1],data1[count+2])
	l1.head = tem_node
	number_data1 -= 1
	count += 2
	while(number_data1 > 0):
		tem_node = node(data1[count+1],data1[count+2])
		l1.add_node(tem_node)
		number_data1 -=1
		count += 2
if number_data2 > 0:
	count = 0
	tem_node = node(data2[count+1],data2[count+2])
	l2.head = tem_node
	number_data2 -= 1
	count += 2
	while(number_data2 > 0):
		tem_node = node(data2[count+1],data2[count+2])
		l2.add_node(tem_node)
		number_data2 -=1
		count +=2


ans_mul = mul(l1,l2)
if len(ans_mul) == 0:
	print(0,0)
else:
	print(" ".join(str(x) for x in ans_mul))
ans_add = sum(add(l1,l2),[])
if len(ans_add) == 0:
	print(0,0)
else:
	print(" ".join(str(x) for x in ans_add))
