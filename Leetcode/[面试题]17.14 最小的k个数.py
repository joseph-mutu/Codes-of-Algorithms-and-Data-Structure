#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-13 15:09:08
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    
    def smallestK(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k < 0 or k > len(arr):
            return arr
        heap = self.create_heap(arr)
        
        k_smallest = []
        for _ in range(k):
            k_smallest.append(self.delete_item(heap))
        return k_smallest
    
    def create_heap(self,arr):
        heap = arr
        heap.insert(0,float('-inf'))
        # find the last parent
        last = (len(arr) - 1)//2
        for parent in range(last,0,-1):
            while parent * 2 < len(heap):
                child = parent * 2
                if child + 1 < len(heap) and heap[child + 1] < heap[child]:
                    child += 1
                if heap[parent] > heap[child]:
                    heap[parent],heap[child] = heap[child],heap[parent]
                else:
                    break
                parent = child
        return heap
    
    def delete_item(self,heap):
        if len(heap) > 1:
            record = heap[1]
            heap[1] = heap[-1]
            pos = 1
            heap.pop()
            while pos * 2 < len(heap) - 1:
                child = pos * 2
                if child + 1 < len(heap) - 1 and heap[child + 1] < heap[child]:
                    child += 1
                if heap[pos] > heap[child]:
                    heap[pos],heap[child] = heap[child],heap[pos]
                else:
                    break
                pos = child
            return record
    
    def inser_item(self,heap,val):
        if not heap:
            heap = [float('-inf')]
        heap.append(val)
        cur_pos = len(heap) - 1

        while heap[cur_pos] < heap[cur_pos//2]:
            parent = cur_pos // 2
            heap[cur_pos],heap[parent] = heap[parent],heap[cur_pos]
            cur_pos = parent
        return heap
    

s = Solution()

x = [1,3,5,7,2,4,6,8]
print(s.smallestK(x,4))
