class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for elem in nums:
            count[elem] = 1 + count.get(elem, 0)
        
        for num, counts in count.items():
            freq[counts].append(num)
        
        result = []
        
        for i in range(len(freq) - 1, 0, -1):
            for elem in freq[i]:
                result.append(elem)
                if (len(result) == k):
                    return result
                