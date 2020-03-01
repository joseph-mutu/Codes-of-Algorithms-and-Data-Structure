#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-29 09:13:19
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class TicTacToe(object):
    """
    一个 TicTacToe 对象可以抽象为一个棋盘，所以该对象要同时保存 2个 player 的状态 
    """

    def __init__(self, n):
        """
        获胜判断方法:
            - 任意一行相加为 n
            - 任意一列相加为 n
            - 左对角线相加为 n
            - 右对角线相加为 n
        """
        # 一个 player 的行状态有 n 个，此处为 2 x n 
        self.row_sum = [[0]*n, [0]*n]
        self.col_sum = [[0]*n, [0]*n]

        self.dia_left_sum = [0,0]
        self.dia_right_sum = [0,0]

        self.target = n

    def move(self, row, col, player):

        self.row_sum[player-1][row] += 1

        self.col_sum[player-1][col] += 1

        if row + col == self.target - 1:
            self.dia_right_sum[player-1] += 1
        if row == col:
            self.dia_left_sum[player-1] += 1

        # 判断是否达到胜利条件
        if self.row_sum[player-1][row] == self.target or \
        self.col_sum[player-1][col] == self.target or \
        self.dia_right_sum[player-1] == self.target or \
        self.dia_left_sum[player-1] == self.target:
            return player

        return 0
