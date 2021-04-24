#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = []
        i,j,k = 0,0,0
        n,m = len(nums1),len(nums2)
        while i < n and j < m:
            if nums1[i] >= nums2[j]:
                res.append(nums2[j])
                j+=1
            else:
                res.append(nums1[i])
                i+=1
                
                
        while i < n:
            res.append(nums1[i])
            i+=1   
        while j < m:
            res.append(nums2[j])
            j+=1
        
        l = len(res)
        if l%2:
            return res[l//2]
        else:
            return (res[l//2]+res[l//2 - 1] ) /2
# @lc code=end

