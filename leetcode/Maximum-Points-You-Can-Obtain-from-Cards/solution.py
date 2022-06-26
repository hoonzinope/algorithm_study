class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k == len(cardPoints):
            return sum(cardPoints)
        
        sum_num = sum(cardPoints)
        window_size = len(cardPoints)-k
        max_num = 0
        part_sum = 0
        for i in range(len(cardPoints)-(window_size-1)):
            if part_sum == 0:
                part_sum = sum(cardPoints[i:i+len(cardPoints)-k])
            else:
                part_sum -= cardPoints[i-1]
                if i+len(cardPoints)-k-1 < len(cardPoints):
                    part_sum += cardPoints[i+len(cardPoints)-k-1]
            # print(cardPoints[i:i+len(cardPoints)-k], part_sum)
            if max_num < (sum_num-part_sum):
                max_num = (sum_num-part_sum)
        return max_num