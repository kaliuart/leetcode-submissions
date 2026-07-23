# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, frequency in frequencies.items():
            buckets[frequency].append(num)

        result = []

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                if len(result) != k:
                    result.append(num)
            
        return result

        