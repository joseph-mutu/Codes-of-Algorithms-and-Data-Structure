#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-04 10:00:53
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = ListNode(float('inf'))
        self.length = 0
        

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.length:
            return -1
        node = self.head
        for _ in range(index+1):
            node = node.next
        return node.val
        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        node = ListNode(val)
        record = self.head.next
        self.head.next= node
        node.next = record
        self.length += 1



    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        new_node = ListNode(val)
        node = self.head
        while node.next:
            node = node.next

        node.next= new_node
        self.length += 1
        

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index >  self.length:
            return 
        elif index == self.length:
            self.addAtTail(val)
            return 
        elif index <= 0:
            self.addAtHead(val)
            return
        node = self.head
        for _ in range(index):
            node = node.next
        record = node.next

        new_node = ListNode(val)
        node.next = new_node
        new_node.next = record
        self.length += 1

        

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index >= self.length:
            return
        elif index  < 0:
            return 
        node = self.head
        for _ in range(index):
            # 找到应该删除的节点的前一个节点
            node = node.next

        record = node.next.next
        del node.next
        node.next = record
        self.length -= 1

s = MyLinkedList()
s.addAtHead(1)
s.addAtTail(3)
# print(s.get(1))
# print(s.head.next.val)
s.addAtIndex(1,2)
# print(s.get(1))
s.deleteAtIndex(0)
print(s.get(0))
["addAtHead","deleteAtIndex","addAtHead","addAtHead","addAtHead","addAtHead","addAtHead","addAtTail","get","deleteAtIndex","deleteAtIndex"]
[[2],[1],[2],[7],[3],[2],[5],[5],[5],[6],[4]]