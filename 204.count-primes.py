#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        
        count = 0          
        primes = [True] * n
        
        for i in range(2, int(n**0.5)+1):
            if not primes[i]:
                continue
            for j in range(i * i, n, i):
                primes[j] = False
        
        for i in range(2, n):
            if primes[i]:
                count += 1
                
        return count
# @lc code=end

