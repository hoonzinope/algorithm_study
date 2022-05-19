def isPrime(num):
    if num == 1:
        return False
    else:
        max_ = int(num**(1/2))
        for x in range(2, max_+1):
            if num % x == 0:
                return False
        return True

def solution(n, k):
    answer = -1
    
    temp_list = []
    while n > 0:
        temp_list.append(str(n%k))
        n //= k
    temp_list.reverse()
    temp = "".join(temp_list)
    temp_list = [n for n in temp.split("0") if n != ""]
    
    result = 0
    for num in temp_list:
        if isPrime(int(num)):
            result+=1
    answer = result
    
    return answer