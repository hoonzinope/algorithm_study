class Solution:
    def candy(self, ratings: List[int]) -> int:
        result = [1] * len(ratings)
        if len(ratings) == 1:
            return sum(result)
        rate_dict = {}
        for i, rate in enumerate(ratings):
            if rate not in rate_dict:
                rate_dict[rate] = [i]
            else:
                rate_dict[rate].append(i)
        
        rate_list = sorted(list(rate_dict.keys()))
        for rate in rate_list:
            index_list = rate_dict[rate]
            for index in index_list:
                if 0 < index and index < len(ratings)-1:
                    curr_ratings = ratings[index]
                    left_ratings = ratings[index-1]
                    right_ratings = ratings[index+1]
                    if left_ratings < curr_ratings and right_ratings < curr_ratings:
                        result[index] = max([result[index-1], result[index+1]])+1
                    elif left_ratings < curr_ratings:
                        result[index] = result[index-1]+1
                    elif right_ratings < curr_ratings:
                        result[index] = result[index+1]+1
                elif index == 0:
                    curr_ratings = ratings[index]
                    right_ratings = ratings[index+1]
                    if right_ratings < curr_ratings:
                        result[index] = result[index+1]+1
                elif index == len(ratings)-1:
                    curr_ratings = ratings[index]
                    left_ratings = ratings[index-1]
                    if left_ratings < curr_ratings:
                        result[index] = result[index-1]+1
        return sum(result)