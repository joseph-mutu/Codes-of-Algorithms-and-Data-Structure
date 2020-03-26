#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-26 06:50:56
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def numRookCaptures(self, board):
        if not board:
            return 0
        # dx,dy 表示上下左右方向的增量
        dx,dy = (-1,1,0,0),(0,0,1,-1)
        sx,sy = -1,-1
        for i in range(7):
            for j in range(8):
                if board[i][j] == 'R':
                    sx,sy = i,j
                    break
        if sx == -1:
            return 0
        num = 0
        #不同方向
        for i in range(4):
            step = 1
            while 1:
                nx = sx + step * dx[i]
                ny = sy + step * dy[i]

                if nx < 0 or nx > 7 or ny < 0 or ny > 7:
                    break
                if board[nx][ny] == 'B':
                    break
                if board[nx][ny] == "p":
                    num += 1
                    break
                step += 1
        return num
graph = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]

s = Solution()
print(s.numRookCaptures(graph))



