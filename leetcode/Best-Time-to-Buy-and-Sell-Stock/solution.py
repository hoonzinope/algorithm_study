class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_num = 10000
        profit = 0
        for price in prices:
            if price < min_num:
                min_num = price
            else:
                temp_profit = price - min_num
                if profit < temp_profit:
                    profit = temp_profit
            # print(price, min_num, profit)
            
        return profit