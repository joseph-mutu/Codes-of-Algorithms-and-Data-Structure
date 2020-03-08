#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-08 08:52:12
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os


class Solution(object):

    def __init__(self):
        self.row = [{'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0} for _ in range(9)]
        self.col = [{'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0} for _ in range(9)]
        self.sub_board = [{'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0} for _ in range(9)]

    def isValidSudoku(self, board):
        if not board:
            return False
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    # 判断当前行是否有重复
                    if self.row[i][board[i][j]] == 0:
                        self.row[i][board[i][j]] += 1
                    else:
                        return False
                    # 判断当前列是否有重复
                    if self.col[j][board[i][j]] == 0:
                        self.col[j][board[i][j]] += 1
                    else:
                        return False

                    # 判断当前格子是否有重复
                    box_num = (i//3) * 3 + (j//3) 
                    if self.sub_board[box_num][board[i][j]] == 0:
                        self.sub_board[box_num][board[i][j]] += 1
                    else:
                        return False
        return True
s = Solution()
board = [
["8","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]
]


print(s.isValidSudoku(board))

