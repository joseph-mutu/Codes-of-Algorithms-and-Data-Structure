#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-27 16:05:48
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

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
        mid = self.find_mid(head)
        # cut off the left part and right part
        right_start = mid.next
        mid.next = None

        reverse_left = self.reverse(head)
        reverse_right = self.reverse(right_start)

        root = self.build_tree(reverse_left)
        right_tree = self.build_tree(reverse_right)

        root.right = right_tree
        return root
        
    # first use two pointers to find the middle of the list
    def find_mid(self,head):
        slow, fast = head,head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    # reverse the list from the middle node
    def reverse(self,node):
        if not node or not node.next:
            return node
        head = self.reverse(node.next)
        # reverse the link
        node.next.next = node
        # link the next of current node to None
        node.next = None
        return head
    
    # construct the tree
    def build_tree(self,root):
        if not root:
            return None
        node = TreeNode(root.val)
        node.left = self.build_tree(root.next)
        return node
        
s = Solution()
head = ListNode(0)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(5)

root = s.sortedListToBST(head)
print(root.val)
# print(root.left.val)
# print(root.right)
# print(root.left.left.val)
# print(root.right.val)
# print(root.right.left.val)