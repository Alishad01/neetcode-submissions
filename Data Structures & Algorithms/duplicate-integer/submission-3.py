class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        memo=[]
        if len(nums)<1:
            return False
        for i in nums:
            if i not in memo:
                memo.append(i)
            else:
                return True
        return False