#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-09 20:40:31
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def exist(self, board, word):
        if not board:
            return False
        if not word:
            return True
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '#' and board[i][j] == word[0]:
                    mark = board[i][j]                    
                    board[i][j] = '#'
                    if self.dfs(i,j,board,word[1:]):
                        return True
                    board[i][j] = mark      
        return False

    def dfs(self,sx,sy,board,word):

        if not word:
            return True
        for nx,ny in ((sx,sy-1),(sx-1,sy),(sx,sy+1),(sx+1,sy)):
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] != '#' and board[nx][ny] == word[0]:
                mark = board[nx][ny]
                board[nx][ny] = '#'
                if self.dfs(nx,ny,board,word[1:]):
                    return True
                board[nx][ny] = mark
                
        return False
            
s = Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(s.exist(board,word))
    