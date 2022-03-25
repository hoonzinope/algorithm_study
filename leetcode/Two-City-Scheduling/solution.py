class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:        
        costs = sorted(costs, key=lambda x : abs(x[0]- x[1]), reverse=True)
        
        a_count = len(costs)//2
        b_count = len(costs)//2
        answer = 0
        for cost in costs:
            if a_count == 0:
                answer += cost[1]
                b_count -= 1
            elif b_count == 0:
                answer += cost[0]
                a_count -= 1
            else:
                if cost[0] < cost[1]:
                    answer+=cost[0]
                    a_count -= 1
                else:
                    answer+=cost[1]
                    b_count -= 1
        return answer