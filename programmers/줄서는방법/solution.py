def solution(n, k):
    answer = []
    def fact(n):
        r = 1
        for i in range(1, n):
            r*=i
        return r
    k -= 1
    numbers = [i for i in range(1, n+1)]
    while len(numbers) > 1:
        r = fact(n)
        index = k // r
        number = numbers.pop(index)
        answer.append(number)
        left = r*index
        k = k - left
        n = n-1
    answer.append(numbers[0])
    # print(answer)
    return answer