class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashy=[]
        if len(nums)<1:
            return False
        for i in nums:
            if i in hashy:
                return True
            else:
                hashy.append(i)
        return False