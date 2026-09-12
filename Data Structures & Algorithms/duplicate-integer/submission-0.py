class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashnet = set()
        for num in nums:
            if num in hashnet:
                return True
            hashnet.add(num)
        return False 
        