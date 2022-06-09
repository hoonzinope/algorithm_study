class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        def binSearch(num_list, num):
            left = 0
            right = len(num_list)
            while left < right:
                mid = (left+right)//2
                if num_list[mid] == num:
                    return mid
                else:
                    if num_list[mid] < num:
                        left = mid+1
                    else:
                        right = mid
            return left
        
        for i, num in enumerate(numbers):
            left = binSearch(numbers[i+1:], target-num)
            add_index = (i+1) + left
            if add_index < len(numbers) and num + numbers[add_index] == target:
                return [i+1, add_index+1]