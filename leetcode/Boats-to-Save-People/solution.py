class Solution:
    def binSearch(self, num, num_list):
        left = 0
        right = len(num_list)
        while left < right:
            mid = (left + right)//2
            if num_list[mid] == num:
                return num_list[mid]
            elif num_list[mid] < num:
                left = mid+1
            else:
                right = mid
        if left >= len(num_list):
            left = len(num_list)-1   
        if num_list[left] > num:
            left -= 1
        return num_list[left]
    
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count = 0
        temp = 0
        people = sorted(people)
        while len(people) > 0:
            temp = people.pop()
            if limit - temp == 0:
                count += 1
                continue
            elif limit - temp > 0:
                if len(people) > 0:
                    add_num = self.binSearch(limit-temp, people)#[x for x in people if x <= limit-temp]
                    if limit-temp >= add_num:
                        index = people.index(add_num)
                        people.pop(index)
                count += 1
            
        return count