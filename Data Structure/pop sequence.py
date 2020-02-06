#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-07 21:05:32
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
import numpy as np

MNK = list(map(int,input().split()))
M = MNK[0]
N = MNK[1]
K = MNK[2]
flag = []
for i in range(K):
	flag.append("YES")
	data = list(map(int,input().split()))
	if data[0] > M:
		flag[i] = "NO"
		continue
	elif abs(data[1] - data[0]) != 1:
		flag[i] = "NO"
		continue
	else:
		for j in range(N-1):
				if data[j+1]<max(data[0],data[j]) and data[j+1] > min(data[0],data[j]):
					flag[i] = "NO"
					break
for i in range(K):
	print(flag[i])
