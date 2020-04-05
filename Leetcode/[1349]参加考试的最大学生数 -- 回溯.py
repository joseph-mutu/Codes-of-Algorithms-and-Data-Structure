#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-03 16:50:59
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$


class Solution(object):
    def __init__(self):
        self.students  = 0
    def maxStudents(self, seats):
        if not seats:
            return 0
        
        valid_seats = []

        for i in range(len(seats)):
            for j in range(len(seats[0])):
                if seats[i][j] == '.':
                    valid_seats.append((i,j))

        self.backtract(-1,valid_seats,seats,0)
        return self.students
    
    def backtract(self,start,valid_seats,seats,nums):
        
        for i in range(start + 1, len(valid_seats)):
            if self.check(valid_seats[i][0],valid_seats[i][1],seats):
                nums += 1
                if nums > self.students:
                    self.students = nums
                seats[valid_seats[i][0]][valid_seats[i][1]] = '1'
                self.backtract(i,valid_seats,seats,nums)
                seats[valid_seats[i][0]][valid_seats[i][1]] = '.'
                nums -= 1
            
    def check(self,x,y,seats):
        directions = ((x,y-1),(x-1,y-1),(x-1,y+1),(x,y+1))
        for nx,ny in directions:
            if 0 <= nx < len(seats) and 0 <= ny <len(seats[0]):

                if seats[nx][ny] == '1':
                    return False
                continue
        return True

s = Solution()
seats = [["#",".",".",".","#"],
[".","#",".","#","."],
[".",".","#",".","."],
[".","#",".","#","."],
["#",".",".",".","#"]]

print(s.maxStudents(seats))