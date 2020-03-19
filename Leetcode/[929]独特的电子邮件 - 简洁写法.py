#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-19 09:20:32
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def numUniqueEmails(self, emails):
        if not emails:
            return 0
        unique = set()
        for email in emails:
            local,domain = email.split('@')
            # deal with +
            if '+' in local:
                local = local[:local.index('+')]
            unique.add(local.replace('.','') + '@' + domain)

        return len(unique)