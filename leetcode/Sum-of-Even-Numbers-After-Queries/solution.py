class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        total = 0
        for num in nums:
            if num % 2 == 0:
                total += num
        
        answer = []
        for query in queries:
            if nums[query[1]] % 2 != 0 and query[0] % 2 != 0:
                nums[query[1]] += query[0]
                total += nums[query[1]]
            elif nums[query[1]] % 2 == 0 and query[0] % 2 == 0:
                total -= nums[query[1]]
                nums[query[1]] += query[0]
                total += nums[query[1]]
            elif nums[query[1]] % 2 == 0 and query[0] % 2 != 0:
                total -= nums[query[1]]
                nums[query[1]] += query[0]
            elif nums[query[1]] % 2 != 0 and query[0] % 2 == 0:
                nums[query[1]] += query[0]
                
            answer.append(total)
        return answer