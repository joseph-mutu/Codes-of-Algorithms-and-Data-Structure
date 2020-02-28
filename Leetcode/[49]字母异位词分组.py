#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-26 08:40:38
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os


class Solution(object):
    def groupAnagrams(self, strs):
        """
        思路：
            遍历所有词，建立一个字典，键：字母排序后的单词，值：存储的index
            遇到一个新词先对其进行排序，然后查找是否已经在字典中，
                若在提取相应的 index
                若不在，则将其排序后添加进字典，并新建一个分组
        """
        if not strs:
            return []
        lookup_dict = {}

        for phrase in strs:
            tem = "".join(sorted(phrase))

            if tem in lookup_dict:
                lookup_dict[tem].append(phrase)
            else:
                lookup_dict[tem] = [phrase]
        return lookup_dict.values()

        # lookup_dict = {}
        # group = []
        # for phrase in strs:

        #     tem = "".join(sorted(phrase))

        #     if tem in lookup_dict:
        #         index = lookup_dict.get(tem)
        #         group[index].append(phrase)
        #     else:
        #         index = len(lookup_dict)
        #         lookup_dict[tem] = index
        #         group.append([phrase])
        return group

s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

