#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-12-02 06:47:10
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
	def exist(self, board, word):
		if not board or not word:
			return False
		visit = [[-1 for i in range(len(board[0]))]for j in range(len(board))]
		for i in range(len(board)):
			for j in range(len(board[0])):
				if self.searchDFS(board,i,j,word,visit,0):
					return True
		return False

	def searchDFS(self,board,startX,startY,word,visit,idx):
		if startX < 0 or startX >= len(board) or startY < 0 or startY >= len(board[0]):
			return False
		if visit[startX][startY] == -1 and board[startX][startY] == word[idx]:
			idx += 1
			if idx == len(word):
				return True
			print(idx)
			visit[startX][startY] = 1
			res = self.searchDFS(board,startX,startY-1,word,visit,idx)\
			or self.searchDFS(board,startX,startY + 1,word,visit,idx) \
			or self.searchDFS(board,startX-1,startY,word,visit,idx) \
			or self.searchDFS(board,startX + 1,startY,word,visit,idx)
			visit[startX][startY] = -1
			idx -= 1
			return res
		return False


s = Solution()
board = [['a']
]
word = "a"
print(s.exist(board,word))