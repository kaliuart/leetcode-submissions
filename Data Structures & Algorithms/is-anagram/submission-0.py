class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(t) != len(s)):
            return False

        d1 = dict()
        d2 = dict()

        for i in range(len(s)):
            d1[s[i]] = d1.get(s[i], 0) + 1
            d2[t[i]] = d2.get(t[i], 0) + 1
        
        return d1 == d2
            
