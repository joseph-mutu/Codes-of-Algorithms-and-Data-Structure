#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-10 09:09:34
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#使用最小堆加速查找

from heapq import heapify,heappush,heappop
class Solution(object):
    def mergeKLists(self, lists):
        if not lists:
            return None
        guard = ListNode(float('inf'))
        head = guard

        heap = []

        for idx,node in enumerate(lists):
            heappush(heap,(node.val,idx))

        while heap:
            _,node,idx = heappop(heap)
            head.next = node
            head = head.next

            next_node = lists[idx].next
            if next_node is None:
                continue
            else:
                heappush(heap,(next_node.val,lists[idx].next,idx))
        
        return guard.next


