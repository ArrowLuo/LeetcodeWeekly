# https://leetcode-cn.com/problems/minimum-subsequence-in-non-increasing-order/

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums = sorted(nums, reverse=True)
        sum_ = sum(nums)
        c_ = [nums[0]]
        for i in range(len(nums)+1):
            c_ = nums[:i+1]
            c_sum_= sum(c_)
            if c_sum_ > sum_ - c_sum_:
                break
        return c_

"""
排序后，因为要求最短且最大。结果一定是顺序元素中第一个满足条件的**连续子数组**。
python中，内置函数sorted的实现算法是Timesort，是一个稳定排序算法。平均时间复杂度为O(nlog(n))，空间复杂度是O(n)。
"""