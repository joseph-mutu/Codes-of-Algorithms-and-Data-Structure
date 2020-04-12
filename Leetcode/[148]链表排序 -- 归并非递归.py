#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-11 17:39:32
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        guard = ListNode(0)
        guard.next = head

        length = 0
        while head:
            head = head.next
            length += 1

        cur_len = 1

        while cur_len < length:

            cur_head,merge_point = guard.next,guard

            while cur_head:
                # 找到第一个 head

                h1,h1_len = cur_head,cur_len

                while cur_head and h1_len:
                    cur_head = cur_head.next
                    h1_len -= 1
                # 如果当前末尾不够 cur_len 的距离，留到下轮
                if h1_len:
                    break

                h2,h2_len = cur_head,cur_len

                while cur_head and h2_len:
                    cur_head = cur_head.next
                    h2_len -= 1
                # 第二段的距离有可能不够 cur_len
                h1_len, h2_len = cur_len,cur_len - h2_len

                # 开始合并
                while h1_len and h2_len:
                    if h1.val > h2.val:
                        merge_point.next = h2
                        merge_point,h2 = merge_point.next,h2.next
                        h2_len -= 1
                    else:
                        merge_point.next = h1
                        merge_point,h1 = merge_point.next,h1.next
                        h1_len -= 1
                #
                if h1_len:
                    merge_point.next = h1
                if h2_len:
                    merge_point.next = h2

                while h1_len > 0 or h2_len > 0:
                    merge_point = merge_point.next
                    h1_len,h2_len = h1_len-1,h2_len-1

                merge_point.next = cur_head

            cur_len *= 2
        return guard.next
s = Solution()
head = ListNode(3)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
nhead = s.sortList(head)
print(nhead.val)
print(nhead.next.val)
print(nhead.next.next.val)
print(nhead.next.next.next.val)








