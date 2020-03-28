#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-28 08:38:04
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Trie:
    def __init__(self):
        self.root = {}
    def insert(self,word):
        node = self.root
        for l in word:
            if l not in node:
                # 创建新的节点
                node[l] = {}
            node = node[l]
        node['end'] = True
    
    def startswith(self,postfix):
        # judege if the postfix matches any
        node = self.root
        for l in postfix:
            if l not in node:
                return False
            node = node[l]
        return True
    

class Solution(object):
    def minimumLengthEncoding(self, words):
        if not words:
            return 0
        # sort by length of words
        words = sorted(words,key = lambda x : len(x),reverse = True)
        words_box = set()
        trie = Trie()
        for word in words:
            word = word[::-1]
            if not words_box:
                trie.insert(word)
                words_box.add(word)
                continue
            if trie.startswith(word):
                continue
            else:
                words_box.add(word)
                trie.insert(word)
            print(words_box)
        return sum(len(word) + 1 for word in words_box)

s = Solution()
print(s.minimumLengthEncoding(["time", "me", "bell"]))