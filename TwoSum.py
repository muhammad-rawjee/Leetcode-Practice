class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevHashMap = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in prevHashMap:
                return [prevHashMap[diff], i]
            
            prevHashMap[num] = i
