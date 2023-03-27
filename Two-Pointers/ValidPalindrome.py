class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1

        while L < R:
            while L < R and not self.isAlphaNum(s[L]):
                L += 1
            while L < R and not self.isAlphaNum(s[R]):
                R -= 1
            if s[L].lower() != s[R].lower():
                return False
            L, R = L + 1, R - 1
        return True

    def isAlphaNum(self, s:str) -> bool:
        return (ord('A') <= ord(s) <= ord('Z') or
                ord('a') <= ord(s) <= ord('z') or
                ord('0') <= ord(s) <= ord('9'))