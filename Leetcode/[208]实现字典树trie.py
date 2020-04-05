#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-28 07:31:58
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        node = self.root
        for l in word:
            if l not in node:
                # 创立节点
                node[l] = {}
            #移动到下一个节点
            node = node[l]
        # 将当前节点进行标记，表示从根节点当前节点为一个单词
        node['end'] = True


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for l in word:
            if l not in node:
                return False
            node = node[l]
        if node.get('end'):
            return True
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for l in prefix:
            if l not in node:
                return False
            node = node[l]
        return True

trie = Trie()

trie.insert("apple")
print(trie.root.keys())
# print(trie.search("apple"))
# # // returns true
# print(trie.search("app"))
# # // returns false
# print(trie.startsWith("app"))
# # // returns true
# print(trie.insert("app"))   
# print(trie.search("app"))     
# # // returns true


 
