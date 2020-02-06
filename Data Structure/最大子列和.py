#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-02 07:42:07
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$
# @Matrix : 6x5(Words:6(corpus))


a = input()
a = int(a)
data = input()
data = data.split(' ')
data = list(map(int,data))
tem_sum = 0
max_sum = -1
start = 0
end = 0
tem_start = 0
for i in range(a):
	tem_sum += data[i]
	if tem_sum < 0:
		tem_sum = 0
		tem_start = i + 1
	if tem_sum > max_sum:
		max_sum = tem_sum
		end = i
		start = tem_start
print(max_sum,data[start],data[end])

