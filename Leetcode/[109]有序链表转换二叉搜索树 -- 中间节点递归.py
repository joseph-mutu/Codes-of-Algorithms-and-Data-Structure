#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-27 17:03:00
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        if not head:
            return None
        mid = self.find_mid(head)
        node = TreeNode(mid.val)
        #只存在一个节点
        if head == mid:
            return node

        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)

        return node


    def find_mid(self,head):
        pre_slow = head
        slow,fast = head,head
        # 如果存在一个节点
        if head.next is None:
            return head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next

        # cut the link between the previous node and the mid mode
        pre.next = None
        return slow


head = ListNode(0)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(5)

s = Solution()
n_head = s.sortedListToBST(head)
