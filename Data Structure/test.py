#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-20 13:44:44
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
import numpy as np
import math







number = int(input())
data = list(map(int,input().split()))
real_order = list(np.full((len(data)),-1,dtype = int))
data = merge_sort(data,real_order)
print(" ".join(str(i) for i in data ))
