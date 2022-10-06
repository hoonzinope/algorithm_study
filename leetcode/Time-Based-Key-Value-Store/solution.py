class TimeMap:

    def __init__(self):
        self.key_time_dict = {}
        self.keyTime_value_dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyTime_value_dict[key+"_"+str(timestamp)] = value
        self.insert(key, timestamp)
        
    def get(self, key: str, timestamp: int) -> str:
        time = self.select(key, timestamp)
        if time < 0:
            return ""
        return self.keyTime_value_dict[key+"_"+str(time)]
    
    def insert(self, key: str, timestamp: int) -> None:
        time_list = []
        if key in self.key_time_dict:
            time_list = self.key_time_dict[key]
        else:
            time_list = []
        
        left = 0
        right = len(time_list)
        mid = (left+right)//2
        while left < right:
            mid = (left+right)//2
            if time_list[mid] == timestamp:
                break
            else:
                if time_list[mid] < timestamp:
                    left = mid+1
                else:
                    right = mid
        if left >= len(time_list):
            time_list.append(timestamp)
        else:
            time_list.insert(left, timestamp)
        self.key_time_dict[key] = time_list
    
    def select(self, key: str, timestamp: int) -> int:
        if key not in self.key_time_dict:
            return -1
        time_list = self.key_time_dict[key]
        left = 0
        right = len(time_list)
        mid = (left+right)//2
        while left < right:
            mid = (left+right)//2
            if time_list[mid] == timestamp:
                left = mid
                break
            else:
                if time_list[mid] < timestamp:
                    left = mid+1
                else:
                    right = mid
        
        if left >= len(time_list):
            return time_list[-1]
        else:
            if time_list[left] > timestamp:
                if left == 0:
                    return -1
                else:
                    return time_list[left-1]
            return time_list[left]
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)