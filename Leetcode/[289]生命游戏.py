#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-01 20:36:21
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def gameOfLife(self, board):
        if not board:
            return []
        # 0 -> 1: -1
        # 1 -> 0: 2
        directions = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
        row = len(board)
        col = len(board[0])
        for i in range(row):
            for j in range(col):
                if board[i][j]  == 0:
                    lives = 0
                    for x,y in directions:
                        if 0 <= i+x < row and 0 <= j+y < col and board[i+x][j+y] >= 1:
                            lives += 1
                    if lives == 3:
                        board[i][j] = -1
                elif board[i][j] == 1:
                    lives = 0
                    for x,y in directions:
                        if 0 <= i+x < row and 0 <= j+y < col and board[i+x][j+y] >= 1:
                            lives += 1
                    if lives < 2 or lives > 3:
                        board[i][j] = 2
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == -1:
                    board[i][j] = 1
        return board
s = Solution()
data = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
print(s.gameOfLife(data))
