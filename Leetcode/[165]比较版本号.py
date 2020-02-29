#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-28 20:00:26
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def compareVersion(self, version1, version2):
        if not version1 and version2:
            return -1
        if version1 and not version2:
            return 1
        if not version1 and not version2:
            return 0



        num_list1 = version1.split('.')
        num_list2 = version2.split('.')

        version1_len = len(num_list1)
        version2_len = len(num_list2)

        for list_idx in range(min(version1_len,version2_len)):
            if int(num_list1[list_idx]) > int(num_list2[list_idx]):
                return 1
            elif int(num_list1[list_idx]) < int(num_list2[list_idx]):
                return -1

        if version1_len > version2_len:
            for version1_list in num_list1[version2_len:]:
                if int(version1_list) > 0:
                    return 1
        elif version1_len < version2_len:
            for version2_list in num_list2[version1_len:]:
                if int(version2_list) > 0:
                    return -1
        return 0
s = Solution()
print(s.compareVersion("1.0","1.0.0.0000"))




