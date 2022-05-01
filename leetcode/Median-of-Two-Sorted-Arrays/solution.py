class Solution:
    def binSearch(self, num_list, num):
        left = 0
        right = len(num_list)
        while left < right:
            mid = (left + right) // 2
            if num_list[mid] == num:
                return mid
            else:
                if num_list[mid] < num:
                    left = mid+1
                else:
                    right = mid
        return left
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        length = 0
        temp_list = []
        
        for num in nums1:
            index = self.binSearch(temp_list, num)
            temp_list.insert(index, num)
            length += 1
            
        for num in nums2:
            index = self.binSearch(temp_list, num)
            temp_list.insert(index, num)
            length += 1
        
        if length % 2 == 1:
            return float(temp_list[length//2])
        else:
            num = (temp_list[length//2-1] + temp_list[length//2]) / 2
            return float(num)
        