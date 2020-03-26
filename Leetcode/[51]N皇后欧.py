#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-25 20:08:39
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

import copy
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n < 0:
            return []
        board = [["."for _ in range(n)] for _ in range(n)]
        results = []

        def place_queens(row,board):

            if row == n:
                tem = ["".join(tem_row) for tem_row in board]
                results.append(copy.deepcopy(tem))
                return 
            #place a queen in the current row,col moves
            for i in range(n):
                if check(row,i,board):
                    # 做出选择
                    board[row][i] = 'Q'
                    place_queens(row+1,board)
                    # 撤销选择
                    board[row][i] = '.'
            return
        
        def check(x,y,board):
            #check the same column,row moves
            for tem_x in range(0,x):
                if board[tem_x][y] == 'Q':
                    # print('same column')
                    return False
            
            # check the left up side
            tem_x,tem_y = x-1,y-1
            while tem_x >=0 and tem_y >=0:
                if board[tem_x][tem_y] == 'Q':
                    # print('left up')
                    return False
                tem_x -= 1
                tem_y -= 1
            
            # check the right up side
            tem_x,tem_y = x-1,y+1
            while tem_x >= 0 and tem_y < n:
                if board[tem_x][tem_y] == 'Q':
                    # print(tem'right up')
                    return False
                tem_x -= 1
                tem_y += 1

            return True
        place_queens(0,board)
        return results
s = Solution()
print(s.solveNQueens(4))