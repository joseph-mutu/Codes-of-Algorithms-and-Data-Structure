#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-26 15:34:51
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os


# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None
        random_dic = {}
        tem_head = head

        #为新链表建立 head 节点的前哨
        guard = Node(-1)
        tem_node = guard

        while tem_head:
            #创建新节点并将前一个节点与其相连
            node = Node(tem_head.val)
            tem_node.next = node

            random_dic[tem_head] = node

            tem_node = tem_node.next

            tem_head = tem_head.next
        
        tem_head1 = head
        tem_head2 = guard.next

        while tem_head1:
            if tem_head1.random is not None:
                tem_head2.random = random_dic[tem_head1.random]
            tem_head1 = tem_head1.next
            tem_head2 = tem_head2.next
        return guard.next

s = Solution()

head = Node(7)
node1 = Node(13)
node2 = Node(11)
node3 = Node(10)
node4 = Node(1)
node1.random = head
node2.random = node4
node3.random = node2
node4.random = head

print(s.copyRandomList(head))
