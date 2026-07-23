# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        data = dict()
        for num in nums:
            data[num] = data.get(num, 0) + 1
            if data[num] > 1:
                return True
        return False
            