class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        ans = set(nums)
        count = 1
        for i in range(1,len(nums)+2):
            if i not in ans:
                return i