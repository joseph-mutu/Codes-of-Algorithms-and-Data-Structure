#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-19 09:29:11
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os


class Solution(object):
    def __init__(self):

        self.heap = [float('-inf')]
        self.size = len(self.heap) - 1
 
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        if not intervals:
            return 0
        intervals.sort()
        for i,j in intervals:
            # 若当前 堆 为空，则添加节点
            if self.size == 0:
                self.insert(j)
            else:
                if self.heap[1] <= i:
                    _ = self.getMin()  
                self.insert(j)

        return self.size

    def insert(self,node):
        """在最小堆中插入一个节点
        Node:
            待插入节点
        操作方法：
            将节点添加入堆的末尾，然后向上调整
        """
        self.heap.append(node)
        self.size += 1
        # print(self.size)
        cur_pos = self.size
        tem_val = node
        # 找出最后一个节点所属的位置
        while tem_val < self.heap[int(cur_pos/2)]:
            self.heap[cur_pos] = self.heap[int(cur_pos/2)]
            cur_pos = int(cur_pos/2)
        # 进行插入
        self.heap[cur_pos] = tem_val

    def getMin(self):
        """提出最小堆的顶端元素，并对最小堆进行调整
        方法：
            - 删除顶端元素
            - 将末尾元素赋给顶端元素
            - call self.alterHeap 对堆进行调整
        """
        pop_val = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1

        self.alterHeap(1)
        self.heap.pop()
        return pop_val

    def alterHeap(self,pos):
        # 给定位置，将当前位置的节点及其子树调整成最小堆
        # 迭代到最后一个具有孩子节点的为止
        tem_val = self.heap[pos]
        while 2*pos <= self.size:
            child = 2*pos
            # 找到左右孩子中小的那一个
            if child != self.size and self.heap[child] > self.heap[child + 1]:
                child += 1
            if tem_val > self.heap[child]:
                self.heap[pos] = self.heap[child]
                pos = child
            else:
                break
        self.heap[pos] = tem_val

    def createHeap(self):
        # 建立堆时，从最后一个有孩子的节点开始，将其调整成最小堆
        for i in range(self.size,0,-1):
            self.alterHeap(i)

heap = [[1905,4041],[1956,5996],[2610,5351],[2047,2967],[3553,5304],[232,5874]]
s = Solution()
print(s.minMeetingRooms(heap))

