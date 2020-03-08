#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-07 07:22:36
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os


class MaxQueue(object):

    def __init__(self):
        self.data_que = []
        self.deque = []


    def max_value(self):
        """
        :rtype: int
        """
        if self.deque:
            return self.deque[0]
        return -1


    def push_back(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.data_que.append(value)
        while self.deque and self.deque[-1] <= value:
            self.deque.pop()
        self.deque.append(value)


    def pop_front(self):
        """
        :rtype: int
        """
        if self.data_que:
            pop_value = self.data_que.pop(0)
            if pop_value == self.deque[0]:
                self.deque.pop(0)
            return pop_value
        return -1

a = MaxQueue()
print()