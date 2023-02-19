class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        anagram_hashset = set()

        for elem in s:
            anagram_hashset.add(elem)

        for elem in t:
            if elem not in s:
                return False
        
        return True
        """
        countT, countS = {}, {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        for elem in countS:
            if countS[elem] != countT.get(elem, 0):
                return False
        
        return True