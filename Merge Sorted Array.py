class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while True:
            if 0 in nums1[m:]:
                nums1.remove(0)
            else:
                break

        while True:
            if 0 in nums2[n:]:
                nums2.remove(0)
            else:
                break

        for k in nums2:
            nums1.append(k)
        nums1.sort()
        return nums1

solution = Solution()
answer = solution.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
print(answer)