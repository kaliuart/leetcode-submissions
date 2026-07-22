class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in d and d[diff] != i:
                return [
                    min(d[diff], i), 
                    max(d[diff], i)
                ]
            else:
                d[nums[i]] = i
            
