#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-14 16:09:43
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.count = 0
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        def dfs(root,tem_sum,pre_nodes):
            if not root:
                return
            tem_sum += root.val
            if tem_sum == sum:
                print(root.val)
                self.count += 1

            tem = tem_sum
            for i in range(len(pre_nodes)):
                tem -= pre_nodes[i]
                if tem == sum:
                    print(root.val,pre_nodes)
                    self.count += 1
            
            pre_nodes.append(root.val)
            dfs(root.left,tem_sum,pre_nodes[:])
            dfs(root.right,tem_sum,pre_nodes[:])
            
            return 
        
        dfs(root,0,[])
        return self.count

s = Solution()
root = TreeNode(1)
root.left = TreeNode(-2)
root.right = TreeNode(-3)
print(s.pathSum(root,-1))


