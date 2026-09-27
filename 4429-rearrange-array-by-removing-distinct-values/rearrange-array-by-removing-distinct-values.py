class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        ans = []
        while nums:
            values = sorted(set(nums))
            for x in values:
                ans.append(x)
                nums.remove(x)
        return ans        
        