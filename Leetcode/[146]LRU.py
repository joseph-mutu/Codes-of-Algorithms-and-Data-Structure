#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-26 08:36:33
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class ListNode(object):
    def __init__(self,key,val):
        self.val = val
        self.key = key
        self.left = None
        self.right = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        # 存储双向链表中的节点
        self.key_dic = {}

        self.head = ListNode(None,float('inf'))
        self.end = ListNode(None,float('inf'))
        self.head.right = self.end
        self.end.left = self.head
         

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.key_dic:
            return -1
        # 将该节点提到 head 之后，也就是最前面
        
        #首先断开该节点
        node = self.key_dic[key]
        pre_node = node.left
        next_node = node.right

        pre_node.right = next_node
        next_node.left = pre_node

        # 将该节点插入头结点之后
        head_next_node = self.head.right
        self.head.right = node
        node.left = self.head

        node.right = head_next_node
        head_next_node.left = node

        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        #当前节点需要插入
        if key not in self.key_dic:
            #首先检查当前节点是否超出了 capacity
            if len(self.key_dic) == self.capacity:
                # 删除最后一个节点
                node = self.end.left
                pre_node = node.left

                pre_node.right = node.right
                self.end.left = pre_node

                del self.key_dic[node.key]
                del node
            
            # 删除之后，将节点插入头结点
            node = ListNode(key,value)
            head_next_node = self.head.right

            self.head.right = node
            node.left = self.head

            head_next_node.left = node
            node.right = head_next_node

            #在字典中记录
            self.key_dic[node.key] = node
        # 当前节点不需要插入，只需要更新
        else:
            # 如果已经存在则直接更新
            self.key_dic[key].key = key
            self.key_dic[key].val = value
            self.get(key)

cache = LRUCache(2);

cache.put(1, 1)
cache.put(2, 2)

print(cache.get(1))       
# # returns 1
print(cache.put(3, 3))    
# # evicts key 2
print(cache.get(2))      
# # returns -1 (not found)
cache.put(4, 4)    
#  # evicts key 1
print(cache.get(1))       
# # returns -1 (not found)
print(cache.get(3))      
# # returns 3
print(cache.get(4))       
# # returns 4
