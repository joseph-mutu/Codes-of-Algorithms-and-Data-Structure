#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-14 16:13:42
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
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
                self.count += 1

            tem = tem_sum
            for i in range(len(pre_nodes)):
                tem -= pre_nodes[i]
                if tem == sum:
                    self.count += 1
            
            pre_nodes.append(root.val)
            dfs(root.left,tem_sum,pre_nodes[:])
            dfs(root.right,tem_sum,pre_nodes[:])
            
            return 
        
        dfs(root,0,[])
        return self.count