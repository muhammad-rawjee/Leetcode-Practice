class Solution:
    def isAnagram(self, s, t) -> bool:
        """
        anagram_hashset = set()

        for elem in s:
            anagram_hashset.add(elem)

        for elem in t:
            if elem not in s:
                return False
        
        return True
        """
        # Set up hash map
        countS, countT = {}, {}
        # Obvious
        if len(s) != len(t):
            return False
        # Fill up Hash Maps
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        # Check for equivalency
        for i in range(len(s)):
            if countS[s[i]] != countT.get(s[i], 0):
                return False
        
        return True
    