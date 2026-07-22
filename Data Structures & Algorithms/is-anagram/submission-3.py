class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(t) != len(s)):
            return False

        arr = [0] * 26

        for i in range(len(s)):
            arr[ord(s[i]) - 97 ] += 1
            arr[ord(t[i]) - 97] -= 1

        for num in arr:
            if num != 0:
                return False
        return True
         
