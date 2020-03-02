#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-02 07:25:41
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
        self.min = None


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.min is None:
            self.min = x
        elif self.min >= x:
            self.data.append(self.min)
            self.min = x
        self.data.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if self.data:
            data = self.data.pop()
            if data == self.min:
                if self.data:
                    self.min = self.data[-1]
                    self.data.pop()
                else:
                    self.min = None
            return data


    def top(self):
        """
        :rtype: int
        """
        return self.data[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.min
minStack = MinStack()
minStack.push(6)
minStack.push(6)
minStack.push(7)
print(minStack.top())
minStack.pop()
print(minStack.getMin()) 
minStack.pop()
print(minStack.getMin())  
minStack.pop()
minStack.push(7)
print(minStack.top())
print(minStack.getMin())  
minStack.push(-8)
print(minStack.top())
print(minStack.getMin())  
minStack.pop()
print(minStack.getMin())  

# ["MinStack","push","push","push","top","pop","getMin",
# "pop","getMin","pop","push","top","getMin","push","top","getMin","pop","getMin"]

# 6 6 7 7 -8

# [null,null,null,null,7,null,6,null,6,null,null,
# 7,7,null,-8,-8,null,7]

# [null,null,null,null,7,null,6,null,6,null,null,
# 7,6,null,-8,-8,null,6]
