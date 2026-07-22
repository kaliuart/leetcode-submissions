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

"""
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for (i, num in enumerate(nums)):
            a.append([num, i])

        a.sort()
        i = 0
        j = len(a) - 1

        while i < j:
            curr = a[i][0] + a[j][0]
            
            if curr == target:
                return [
                min(a[i][1], a[j][1]),
                max(a[i][1], a[j][1])
                
                ]
            
            elif curr < target:
                i++
            
            else:
                j--
        return []
"""
            
