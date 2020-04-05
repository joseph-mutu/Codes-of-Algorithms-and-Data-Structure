#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-05 07:13:24
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

import collections

class Node:
    def __init__(self,key,val,freq = 0, pre = None, next = None):
        self.key = key
        self.val = val
        self.freq = freq
        self.pre = pre
        self.next = next

    def insert(self,next):
        # next is the node that will be inserted
        next.next = self.next
        self.next.pre = next

        next.pre = self
        self.next = next

def double_linked():
    head = Node(-1,float('inf'))
    tail = Node(-1,float('-inf'))

    head.next = tail
    tail.pre = head
    return (head,tail)

class LFUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.min_freq = 0
        #there is a dobule linked list in each distinct frequency
        self.freq_map = collections.defaultdict(double_linked)
        self.key_map = {}
        self.size = 0

    def delete(self,node):
        if node.pre:
            node.pre.next = node.next
            node.next.pre = node.pre

            # 如果删除的是当前 freq 中唯一的节点，则删除整个双向链表
            if node.pre is self.freq_map[node.freq][0] and node.next is self.freq_map[node.freq][-1]:
                self.freq_map.pop(node.freq)
        return node.key

    def increase(self,node):
        node.freq += 1
        self.delete(node)

        # 插入到更高 freq 中的尾节点上
        self.freq_map[node.freq][-1].pre.insert(node)

        # 维护最小 freq
        if node.freq == 1:
            self.min_freq = 1
        elif self.min_freq == node.freq - 1:
            #如果将当前节点提出后，原最小freq 中没有了节点
            if self.freq_map[self.min_freq][0].next is self.freq_map[self.min_freq][-1]:
                self.freq_map.pop(self.min_freq)
                self.min_freq = node.freq

    def get(self, key):

        if key in self.key_map:
            node = self.key_map[key]
            self.increase(node)
            return node.val
        else:
            return -1
    def put(self, key, value):
        if self.capacity != 0:
            if key in self.key_map:
                node = self.key_map[key]
                node.val = value
            else:
                # 如果不在当前 key map 中，则创建新的节点
                self.size += 1
                node = Node(key,value)
                self.key_map[key] = node

            #判断是否删除节点
            if self.size > self.capacity:
            #     print('size:',self.size)
            #     print('evict node:',self.freq_map[self.min_freq][0].next.val)

                deleted = self.delete(self.freq_map[self.min_freq][0].next)
                self.size -= 1
                self.key_map.pop(deleted)
            self.increase(node)

cache = LFUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))       
# // returns 1
print(cache.put(3, 3))    
# # // evicts key 2
print(cache.get(2))       
# # // returns -1 (not found)
print(cache.get(3))       
# # // returns 3.
print(cache.put(4, 4))    
# # // evicts key 1.
print(cache.get(1))       
# # // returns -1 (not found)
print(cache.get(3))       
# # // returns 3
print(cache.get(4))       
# # // returns 4
