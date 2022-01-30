class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last = 0
        for _ in range(k):
            last = nums[len(nums)-1]
            nums.insert(0, last)
            nums.pop()
