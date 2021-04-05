class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        p = sorted([i for i in s])
        q = sorted ([j for j in t])
        return p == q
