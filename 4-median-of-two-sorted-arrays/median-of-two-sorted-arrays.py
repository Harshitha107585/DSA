class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        ans = nums1+nums2
        ans.sort()

        total = len(ans)

        if total % 2 == 1:
            return float(ans[total // 2])
        else:
            mid1 = ans[total//2-1]
            mid2 = ans[total // 2]
            return (float(mid1)+float(mid2)) / 2.0    