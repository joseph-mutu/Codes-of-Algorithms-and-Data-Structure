#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-07 20:53:18
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
class Solution(object):
    def exist(self, board, word):
        if not board or not word:
            return False
        visit = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visit[i][j] = 1
                    if self.searchDFS(board,i,j,word[1:],visit):
                        return True
                    visit[i][j] = 0
        return False

    def searchDFS(self,board,i,j,word,visit):
        # print(board[i][j],i,j,word)
        if not word:
            return True

        def neighbour(i,j):
            for new_i,new_j in ((i-1,j),(i,j+1),(i+1,j),(i,j-1)):
                if new_i >= 0 and new_i < len(board) and new_j >=0 \
                and new_j < len(board[0]):
                    yield new_i,new_j

        for new_i,new_j in neighbour(i,j):
            if visit[new_i][new_j] == 0 and board[new_i][new_j] == word[0]:
                visit[new_i][new_j] = 1
                if self.searchDFS(board,new_i,new_j,word[1:],visit):
                    return True
                visit[new_i][new_j] = 0
        return False

s = Solution()
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
print(s.exist(board,"ABCCED"))

