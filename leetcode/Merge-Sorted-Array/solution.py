class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        remove_length = len(nums2)
        while len(nums2) != 0:
            temp_num = nums2.pop(0)
            index = nums1.index(0)
            nums1[index] = temp_num
        nums1.sort()
