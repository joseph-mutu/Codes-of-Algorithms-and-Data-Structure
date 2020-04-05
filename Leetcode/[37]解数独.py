#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-04 19:38:20
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

import copy
class Solution(object):
    def __init__(self):
        self.find = False
        self.results = []
    def solveSudoku(self, board):
        #统计每个数独方块中出现的数字
        blocks = [set() for _ in range(9)]
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        #统计哪些点需要被填入
        empty = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    block = self.get_num(i,j)
                    # 将当前已有的数根据方块进行统计
                    blocks[block].add(board[i][j])
                    # 统计行
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                elif board[i][j] == '.':
                    empty.append([i,j])
        board = self.backtrack(board,empty,blocks,row,col)


    def backtrack(self,board,empty,blocks,row,col):
        if not empty:
            self.find = True
            return board
        x,y = empty[0]
        for i in ['1','2','3','4','5','6','7','8','9']:
            if self.find:
                return board
            block = self.get_num(x,y)
            if self.is_valid(x,y,i,block,board,blocks,row,col):
                board[x][y] = i
                blocks[block].add(i)
                row[x].add(i)
                col[y].add(i)
                self.backtrack(board,empty[1:],blocks,row,col)
                if self.find:
                    return board
                board[x][y] = '.'
                blocks[block].remove(i)
                row[x].remove(i)
                col[y].remove(i)

    def is_valid(self,x,y,val,block,board,blocks,row,col):
        if val in blocks[block]:
            return False
        if val in row[x]:
            return False
        if val in col[y]:
            return False
        return True

    def get_num(self,x,y):
        # 根据横纵坐标计算当前点属于哪一个方块
        return (x//3)*3 + y//3 
s = Solution()
graph = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print(s.solveSudoku(graph))