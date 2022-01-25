class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        max_num = max(arr)
        max_index = arr.index(max_num)
        
        if max_index == 0 or max_index == len(arr)-1:
            return False
        else:
            for i in range(1, max_index):
                if arr[i-1] >= arr[i]:
                    return False

            for i in range(max_index, len(arr)-1):
                if arr[i] <= arr[i+1]:
                    return False
                
        return True