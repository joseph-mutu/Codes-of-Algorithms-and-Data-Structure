#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-29 07:13:52
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def coinChange(self, coins, amount):
        """
        利用贪心算法，从硬币最大面值开始匹配
        """
        if not coins or amount < 0:
            return -1
        dp = [amount + 1 for _ in range(amount+1)]
        dp[0] = 0
        for money in range(1,amount + 1):
            for coin in coins:
                if coin > money:
                    continue
                dp[money] = min(dp[money],1 + dp[money - coin])

        return dp[amount] if dp[amount] < amount + 1 else -1


s = Solution()
print(s.coinChange([2],3))






