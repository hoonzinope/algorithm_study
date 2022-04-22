class MyHashMap:
    
    temp_list = []
    def __init__(self):
        self.temp_list = []

    def put(self, key: int, value: int) -> None:
        if len(self.temp_list) == 0:
            self.temp_list.append([key,value])
        else:
            num_list = [num[0] for num in self.temp_list]
            index = self.binSearch(num_list, key)
            if index < len(self.temp_list):
                if self.temp_list[index][0] == key:
                    self.temp_list[index][1] = value
                else:
                    self.temp_list.insert(index, [key, value])
            else:
                self.temp_list.append([key, value])

    def get(self, key: int) -> int:
        num_list = [num[0] for num in self.temp_list]
        index = self.binSearch(num_list, key)
        if index < len(self.temp_list):
            if self.temp_list[index][0] == key:
                return self.temp_list[index][1]
            else:
                return -1
        else:
            return -1

    def remove(self, key: int) -> None:
        num_list = [num[0] for num in self.temp_list]
        index = self.binSearch(num_list, key)
        if index < len(self.temp_list):
            if self.temp_list[index][0] == key:
                self.temp_list.pop(index)
        
    def binSearch(self, num_list, num):
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

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)