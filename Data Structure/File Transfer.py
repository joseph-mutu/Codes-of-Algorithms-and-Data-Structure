#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-22 14:05:36
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
import numpy as np


def find_root(data,mess):
	while data[mess] > 0:
		mess = data[mess]
	return int(mess)

def find_com(data):
	com = 0
	for i in range(len(data)):
		if data[i] < 0:
			com += 1
	return com


number_com = int(input())
data = [-1 for i in range(number_com)]

while 1:
	mess = list(input().split())
	if mess[0] == 'S':
		number = find_com(data)
		if number > 1:
			print("There are",number,"components.")
			break
		else:
			print("The network is connected.")
			break
	else:
		if mess[0] == 'I':
			mess[1] = int(mess[1]) - 1
			mess[2] = int(mess[2]) - 1
			if data[mess[1]] < 0 and data[mess[2]] < 0 :
				if np.abs(data[mess[1]]) > np.abs(data[mess[2]]) :
					data[mess[2]] = mess[1]
					data[mess[1]] -= 1

				else:
					data[mess[1]] = mess[2]
					data[mess[2]] -= 1
			elif data[mess[1]] < 0 and data[mess[2]] > 0 :
				root = find_root(data,mess[2])
				data[mess[1]] = root
				data[root] -= 1
			elif data[mess[1]] > 0  and data[mess[2]] < 0 :
				root = find_root(data,mess[1])
				data[mess[2]] = root
				data[root] -= 1
		if mess[0] == 'C':
			mess[1] = int(mess[1]) - 1
			mess[2] = int(mess[2]) - 1
			if find_root(data,mess[1]) == find_root(data,mess[2]):
				print("yes")
			else:
				print("no")


