def solution(elements):
    answer = 0
    length = len(elements)
    elements += elements
    sum_set = set()
    for i in range(1, length+1):
        total = sum(elements[0:i])

        sum_set.add(total)
        for j in range(0, length):
            total -= elements[j]
            total += elements[i+j]
            sum_set.add(total)
    
    answer = len(sum_set)
    return answer