#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-12-12 06:47:45
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

# class TreeNode(object):
# 	def __init__(self, x):
# 		self.val = x
# 		self.left = None
# 		self.right = None

class Solution:
	def buildTree(self, preorder, inorder):
		if not preorder or not inorder:
			return None
		cur_node = TreeNode(-1)
		cur_node = self.buildNode(cur_node,0,0,len(preorder),preorder,inorder)

		return cur_node

	def buildNode(self,cur_node,preStart,inStart,length,preorder,inorder):
		if length == 0:
			return
		elif length == 1:
			return TreeNode(preorder[preStart])
		else:
			cur_pre = preorder[preStart]
			mid_pos = inorder.index(cur_pre)

			left_length = mid_pos - inStart 
			right_length = length - left_length - 1

			tem_node = TreeNode(preorder[preStart])
			cur_node = tem_node

			# deal with the left subtree
			cur_node.left = self.buildNode(cur_node.left,preStart+1,inStart,left_length,preorder,inorder)
			cur_node.right = self.buildNode(cur_node.right,preStart + left_length + 1,mid_pos+ 1,right_length,preorder,inorder)

			return cur_node

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
s = Solution()
node = s.buildTree(preorder,inorder)
print(node.val)
print(node.left.val)
print(node.right.val)
print(node.right.left.left)

