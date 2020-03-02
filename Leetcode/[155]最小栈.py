#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-02 06:48:56
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min = []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.data.append(x)
        if not self.min or x <= self.min[-1]:
            self.min.append(x)


    def pop(self):
        """
        :rtype: None
        """
        if self.data:
            data = self.data.pop()
            if data == self.min[-1]:
                self.min.pop()
        else:
            data = None
        return data

    def top(self):
        """
        :rtype: int
        """
        if self.data:
            data = self.data[-1]
        else:
            data = None
        return data


    def getMin(self):
        """
        :rtype: int
        """
        if self.min:
            return self.min[-1]


minStack = MinStack();
minStack.push(0);
minStack.push(1);
minStack.push(0);
print(minStack.getMin());  # --> Returns -3.
minStack.pop();
# minStack.top();     # --> Returns 0.
print(minStack.getMin());  # --> Returns -2.


