from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        result = defaultdict(list)

        for string_val in strs:
            char_count = [0] * 26

            for char in string_val:
                char_count[ord(char) - ord('a')] += 1

            result[tuple(char_count)].append(string_val)
        
        return result.values()
    

# Testing
strs = ["eat","tea","tan","ate","nat","bat"]

ali = Solution()
print(ali.groupAnagrams(strs))
