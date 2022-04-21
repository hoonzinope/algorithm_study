class MyHashSet:
    temp_list = []
    def __init__(self):
        self.temp_list = []        

    def add(self, key: int) -> None:
        index = self.binSearch(key)
        if index < len(self.temp_list) and self.temp_list[index] == key:
            pass
        else:
            self.temp_list.insert(index, key)

    def remove(self, key: int) -> None:
        index = self.binSearch(key)
        if index < len(self.temp_list) and self.temp_list[index] == key:
            self.temp_list.pop(index)

    def contains(self, key: int) -> bool:
        index = self.binSearch(key)
        if index < len(self.temp_list) and self.temp_list[index] == key:
            return True
        else:
            return False
        
    def binSearch(self,num):
        num_list = self.temp_list
        left = 0
        right = len(num_list)
        while left < right:
            mid = (left+right) // 2
            if num_list[mid] == num:
                return mid
            else:
                if num_list[mid] > num:
                    right = mid
                elif num_list[mid] < num:
                    left = mid+1
        return left
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)