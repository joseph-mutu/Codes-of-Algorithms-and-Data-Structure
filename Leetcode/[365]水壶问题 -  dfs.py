#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-21 07:42:15
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def canMeasureWater(self, x, y, z):
        if z < 0:
            return False
        elif z == 0:
            return True
        #存储dfs中的 state，避免出现循环
        state = set()
        return self.dfs(x,y,z,state,x,y)

    
    def dfs(self,x,y,z,state,x_upper,y_upper):
        if x + y == z:
            return True
        if (x,y) in state:
            return False
        print(x,y)
        print('*'*20`)
        state.add((x,y))

        #将一个或者两个罐子全部装满水
        if self.dfs(x_upper,y,z,state,x_upper,y_upper) or self.dfs(x,y_upper,z,state,x_upper,y_upper) or self.dfs(x_upper,y_upper,z,state,x_upper,y_upper):
            return True
        
        #将一个或者两个罐子全部清空
        elif self.dfs(0,y,z,state,x_upper,y_upper) or self.dfs(x,0,z,state,x_upper,y_upper) or self.dfs(0,0,z,state,x_upper,y_upper):
            return True
        # 将 y 的水全部倒入 x，分为两种情况
        #第一种: y 的水倒入 x 中，x 不满
        # 第二种: y 的水倒入 x 中，x 会多
        elif (x_upper>= x + y and self.dfs(x+y,0,z,state,x_upper,y_upper)) or (x_upper< x+y and self.dfs(x_upper, y - (x_upper-x),z,state,x_upper,y_upper)):
            return True
        #将 x 的水倒入 y 中，分为两种情况
        # 第一种: x 倒入 y，y 不满，此时 x 为空
        # 第二种：x 倒入 y，y 满，此时 x 有剩余
        elif (y_upper >= x + y and self.dfs(0,x+y,z,state,x_upper,y_upper)) or (y_upper < x + y and self.dfs(x - (y_upper - y),y_upper,z,state,x_upper,y_upper)):
            return True
        return False

s = Solution()
print(s.canMeasureWater(104579,104593,12444))