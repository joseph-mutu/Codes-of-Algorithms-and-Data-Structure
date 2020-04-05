#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-03 21:18:30
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}


    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        node = self.root
        for letter in word:
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node['end'] = True


    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for idx,letter in enumerate(word):
            if letter not in node:
                if letter  == '.':
                    if self.backtrack(node,word[idx:]):
                        return True
                    else:
                        return False
                else:
                    return False
            node = node[letter]
        if node.get('end'):
            return True
        return False

    def backtrack(self,node,word):
        if not word:
            if node.get('end'):
                return True
            else:
                return False

        if word[0] == '.':
            children = node.keys()
            for child in children:
                if child is not 'end' and self.backtrack(node[child],word[1:]):
                    return True
        else:
            if word[0] in node:
                if self.backtrack(node[word[0]],word[1:]):
                    return True
            else:
                return False
        return False 

s = WordDictionary()
# [[],["at"],["and"],["an"],["add"],["a"],[".at"],["bat"],
# [".at"],["an."],["a.d."],["b."],["a.d"],["."]]
s.addWord('at')
s.addWord('and')
s.addWord('an')
s.addWord('add')
print(s.search('.at'))
s.addWord('bat')
print(s.search('battt'))
print(s.search('an.'))
print(s.search('a.d.'))
print(s.search('b.'))