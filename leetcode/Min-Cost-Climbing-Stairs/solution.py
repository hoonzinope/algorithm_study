class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        result = [cost[0],cost[1]]
        for i in range(2, len(cost)):
            result.append(min(result[i-2]+cost[i], result[i-1]+cost[i]))
        return min(result[-2], result[-1])