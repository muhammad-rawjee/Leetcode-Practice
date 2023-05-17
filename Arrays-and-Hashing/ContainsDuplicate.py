
class Solution:
    def containsDuplicate(self, nums) -> bool:
        

        hash_set = set()

        for elem in nums:
            if elem in hash_set:
                return True
            hash_set.add(elem)

        return False
ali = Solution()

print(ali.containsDuplicate([1,2,4]))
