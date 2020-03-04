#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-04 10:02:55
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os


class Solution(object):
    def solve(self, board):
        if not board:
            return board

        row_len = len(board)
        col_len = len(board[0])

        visit = [[0 for _ in range(col_len)]for _ in range(row_len)]

        def neighbour(x,y):

            for nx,ny in ((x-1,y),(x,y+1),(x+1,y),(x,y-1)):
                if nx >= 0 and nx < row_len and ny >= 0 and ny < col_len and \
                board[nx][ny] != 'X' and visit[nx][ny] == 0:
                    yield nx,ny

        def dfs(x,y,visit):
            visit[x][y] = 1
            
            for nx,ny in neighbour(x,y):

                visit = dfs(nx,ny,visit)

            return visit

        for i in range(col_len):
            if board[0][i] == 'O':
                visit = dfs(0,i,visit)
            if board[row_len-1][i] == 'O' and visit[row_len-1][i] != 1:
                visit = dfs(row_len-1,i,visit)

        for i in range(row_len):
            if board[i][0] == 'O' and visit[i][0] != 1:
                visit = dfs(i,0,visit)
            if board[i][col_len-1] == 'O' and visit[i][col_len - 1] != 1:
                visit = dfs(i,col_len - 1, visit)

        for i in range(row_len):
            for j in range(col_len):
                if visit[i][j] == 0:
                    board[i][j] = 'X'
s = Solution()
data = [['X','X','X','X'],
['X','O','O','X'],
['X','O','O','X'],
['X','X','X','O']]
s.solve(data)



