# 1920. Build Array from Permutation
# https://leetcode.com/problems/build-array-from-permutation/

from typing import List


class Solution:

    def buildArray(self, nums: List[int]) -> List[int]:
        ret = []
        for i in range(len(nums)):
            ret.append(nums[nums[i]])
        return ret
