#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-04 11:32:08
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

''' 
1. 当 put 一个键值对的时候，如果已经存在相应的键，则重写该值
2. 当 get 一个键时，将相应的节点提取到 head 之后
3. 一个 Hash 表中键为 key （一个值），其存储的即为双向链表中的节点地址
'''
 
class ListNode(object):
    def __init__(self,key = None, value = None):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.hashmap = {}
        self.head = ListNode(-1)
        self.tail = ListNode(-1)

        self.head.next = self.tail
        self.tail.prev = self.head 
    
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.hashmap.get(key,0):
            cur_node = self.hashmap.get(key)

            cur_node.next.prev = cur_node.prev
            cur_node.prev.next = cur_node.next

            tem_node = self.head.next
            self.head.next = cur_node
            cur_node.next = tem_node
            cur_node.prev = self.head
            tem_node.prev = cur_node


            # print('当前节点',cur_node.value)
            return cur_node.value
        else:
            # print(-1)
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # when it exceeds the max capacity,
        # delete the last node 
        # before the tail and del the corresponding dic
        if not self.hashmap.get(key,0) and len(self.hashmap) >= self.capacity:

            del_node = self.tail.prev
            tem_node = del_node.prev

            tem_node.next = self.tail
            self.tail.prev = tem_node

            tem_key = del_node.key
            # print('del_node',del_node.value)
            del self.hashmap[tem_key]
            del del_node

        if self.hashmap.get(key,0):
            cur_node = self.hashmap.get(key)
            cur_node.value = value

            cur_node.next.prev = cur_node.prev
            cur_node.prev.next = cur_node.next

        else:
            cur_node = ListNode(key,value)
            self.hashmap[key] = cur_node

        tem_node = self.head.next
        self.head.next = cur_node
        cur_node.next = tem_node
        cur_node.prev = self.head
        tem_node.prev = cur_node

cache = LRUCache(2)
cache.put(1, 1);
cache.put(2, 2);

cache.get(1);       # 返回  1
cache.put(3, 3);    # 该操作会使得密钥 2 作废

cache.get(2);       # 返回 -1 (未找到)
cache.put(4, 4);    # 该操作会使得密钥 1 作废
cache.get(1);       # 返回 -1 (未找到)
cache.get(3);       # 返回  3
cache.get(4);       # 返回  4

