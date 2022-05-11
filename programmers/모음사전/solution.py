vow = ['A', 'E', 'I', 'O', 'U']
result = []
def dfs(val):
    if len(val) == 5:
        result.append(val)
        return
    else:
        result.append(val)
        for v in vow:
            dfs(val+v)
        return
    
def solution(word):
    answer = 0
    
    for v in vow:
        dfs(v)
    
    answer = result.index(word) + 1
    return answer