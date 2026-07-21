class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo={}
        for i, num in enumerate(nums):
            
            if target-num in memo:
                return [memo[(target-num)], i] 
            memo[num]=i           
        return []