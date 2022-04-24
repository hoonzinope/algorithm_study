class UndergroundSystem:
    temp_dict = dict()
    timeTaken = dict()
    def __init__(self):
        self.temp_dict = dict()
        self.timeTaken = dict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.temp_dict[id] = {"station":stationName, "time":t}
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_info = self.temp_dict[id]
        
        key = (start_info['station'], stationName)
        if key in self.timeTaken:
            self.timeTaken[key].append(t - start_info['time'])
        else:
            self.timeTaken[key] = [t - start_info['time']]
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        key = (startStation, endStation)
        sum_num = sum(self.timeTaken[key])
        length = len(self.timeTaken[key])
        return sum_num / length


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)