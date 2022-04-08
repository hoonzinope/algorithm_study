class KthLargest:
    
    def __init__(self, k: int, nums: List[int]):
        self.temp_list = sorted(nums)
        self.index = k

    def add(self, val: int) -> int:
        insert_index = self.binSearch(self.temp_list, val)
        self.temp_list.insert(insert_index, val)
        return self.temp_list[-self.index]
        
    def binSearch(self, temp_list: List[int] , k : int):
        left = 0
        right = len(temp_list)
        while left < right:
            mid = (left + right) // 2
            if temp_list[mid] == k:
                return mid
            else:
                if temp_list[mid] > k:
                    right = mid
                else:
                    left = mid+1
        return left

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)