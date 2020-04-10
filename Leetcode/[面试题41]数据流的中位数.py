#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-10 08:10:41
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

from heapq import heappop,heappush
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []
        self.min_heap = []


    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        #保证两边的数据平衡
        # 当数据为偶数的时候，插入最大堆
        # 当数据为奇数的时候，插入最小堆

        #两者相等一定为偶数
        if len(self.max_heap) == len(self.min_heap):
            #保证最大堆中所有元素小于最小堆
            #先插入最小堆，然后将最小堆元素插入最大堆
            heappush(self.max_heap, -heappushpop(self.min_heap,num))
        else:
            # 插入最小堆，保证最大堆中所有元素小于最小堆
            # 先插入最大堆，再插入最小堆
            heappush(self.max_heap,-num)
            heappush(self.min_heap,-heappop(self.max_heap))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.max_heap) == len(self.min_heap):
            num1 = -self.max_heap[0]
            num2 = self.min_heap[0]
            return (num1+num2) /2.0
        else:
            num = self.max_heap[0]
            return num/1.0
