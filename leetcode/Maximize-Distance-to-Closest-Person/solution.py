class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        max_dist = 0
        for i, seat in enumerate(seats):
            if seat==0:
                left_dist=1 
                left_flag = False
                temp_left = list(reversed(seats[:i]))
                for ls in temp_left:
                    if ls == 1:
                        left_flag = True
                        break
                    else:
                        left_dist += 1
                right_dist=1
                right_flag = False
                # print(temp_left,seats[i+1:])
                for rs in seats[i+1:]:
                    if rs == 1:
                        right_flag = True
                        break
                    else:
                        right_dist += 1
                if left_flag and right_flag:
                    if left_dist > right_dist:
                        if max_dist < right_dist:
                            max_dist = right_dist
                    else:
                        if max_dist < left_dist:
                            max_dist = left_dist
                else:
                    if left_flag and not right_flag:
                        if max_dist < left_dist:
                            max_dist = left_dist
                    elif right_flag and not left_flag:
                        if max_dist < right_dist:
                            max_dist = right_dist
                        
                # print(left_dist, right_dist)    
        return max_dist