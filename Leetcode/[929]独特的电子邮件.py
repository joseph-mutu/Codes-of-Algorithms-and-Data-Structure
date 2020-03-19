#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-19 09:13:13
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

import collections
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        if not emails:
            return 0
        # a dic whose key is domain and the value is a list of unique addresses
        domain_local = collections.defaultdict(list)
        num_email = 0
        for email in emails:
            email = email.split('@')
            local = email[0]
            local_dot = local.count('.')
            local_plus = local.count('+')
            if not local_dot and not local_plus and local not in domain_local[email[1]]:
                print(local)
                domain_local[email[1]].append(local)
                num_email += 1
            else:
                local = list(local)
                for _ in range(local_dot):
                    local = local[:local.index('.')] + local[local.index('.')+1:]
                if local_plus:
                    local = local[:local.index('+')]
                local = "".join(local)
                if local not in domain_local[email[1]]:
                    domain_local[email[1]].append(local)
                    num_email += 1
            print(domain_local)
        return num_email
        

s = Solution()
print(s.numUniqueEmails(["abc@def.com","abcd@ef.com","ab.c@def.com"]))