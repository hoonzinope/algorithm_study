def solution(n):
    answer = 0
    num_dict = {}
    num_dict[0] = 0
    num_dict[1] = 1
    num_dict[2] = 2

    def permutations(arr, n):
        if n in num_dict:
            return num_dict[n]

        total = 0
        for (i, num) in enumerate(arr):
            if n-num >= 0:
                if n-num in num_dict:
                    total += num_dict[n-num] % 1234567
                else:
                    total += permutations(arr, n-num) % 1234567
        num_dict[n] = total % 1234567
        return total
    
    for i in range(0, n+1):
        permutation = permutations([1,2], i)
    answer = num_dict[n] % 1234567
    return answer