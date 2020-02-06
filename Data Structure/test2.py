#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-10 06:36:43
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
import numpy as np

data = [3,4,6,5,7,8,9]
pair = int(len(data)/4)
for i in range(pair):
	print(i)
print(pair*i + 4)