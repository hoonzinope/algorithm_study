class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def binSearch(temp_list, num):
            left = 0
            right = len(temp_list)
            while left < right:
                mid = (left + right) // 2
                if temp_list[mid] == nums:
                    return mid
                else:
                    if temp_list[mid] < num:
                        left = mid+1
                    else:
                        right = mid
            return left
        
        temp_list = []
        for num in nums:
            index = binSearch(temp_list, num)
            temp_list.insert(index, num)
        
        add_num = 0
        if len(nums) % 2 != 0:
            add_num = 1
        
        pre = temp_list[:len(temp_list)//2+add_num][::-1]
        post = temp_list[len(temp_list)//2+add_num:][::-1]
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = pre.pop(0)
            else:
                nums[i] = post.pop(0)