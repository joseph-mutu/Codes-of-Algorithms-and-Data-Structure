#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-10 09:22:42
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os


class Solution(object):
    def mergeKLists(self, lists):
        if not lists:
            return None
        return self.merge(0,len(lists)-1,lists)

    def merge(self,l,r,lists):
        if l == r:
            return lists[l]

        mid = (l +r )//2
        list1 = self.merge(l,mid,lists)
        list2 = self.merge(mid +1,r,lists)

        return self.merge_two(list1,list2)

    def merge_two(self,list1,list2):
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val > list2.val:
            list2.next = self.merge_two(list1,list2.next)
            return list2
        elif list1.val <= list2.val:
            list1.next = self.merge_two(list1.next,list2)
            return list1
