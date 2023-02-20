class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for word in strs:
            char_count = [0] * 26

            for char in word:
                char_count[ord(char) - ord("a")] += 1
            
            result[tuple(char_count)].append(word)
        
        return result.values()