class Solution:
    def binSearch(self, num, num_list):
        left = 0
        right = len(num_list)
        while left < right:
            mid = (left + right) // 2
            if num_list[mid] == num:
                return mid
            else:
                if num_list[mid] < num:
                    left = mid+1
                elif num_list[mid] > num:
                    right = mid
        return -1
    
    def search(self, nums: List[int], target: int) -> bool:
        
        index = 0
        for i in range(1,len(nums)):
            if nums[i-1] > nums[i]:
                index = i
        
        new_num_list = nums[index:] + nums[:index]
        result = self.binSearch(target, new_num_list)
        if result == -1:
            return False
        else:
            return True