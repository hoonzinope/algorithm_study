class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_num = 0
        for account in accounts:
            sum_num = sum(account)
            if max_num < sum_num:
                max_num = sum_num
                
        return max_num