from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        someHashMap = {}

        for i in range(len(nums)):
            checkVal = target - nums[i]
            if checkVal in someHashMap:
                return [i, checkVal]
            
            someHashMap[nums[i]] = i