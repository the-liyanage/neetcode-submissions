class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        empty_list =[]
        for i in range(2):
            for num in nums:
                empty_list.append(num)
        return empty_list
        