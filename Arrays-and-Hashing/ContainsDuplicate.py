class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        '''
        for i in range(len(nums)):
            if nums[i] in nums[i + 1:]:
                return True
        return False
        '''

        hashset = set()

        for num in nums:
            if num in hashset:
                return True
            
            hashset.add(num)

        return False
