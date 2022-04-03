def dfs(oper, operations, expression):
    expressions = expression.split(oper)
    if len(operations) == 0:
        return eval(expression)
    else:
        result_list = []
        if oper == "+":
            for oper_ in operations:
                new_operations = list(operations)
                new_operations.remove(oper_)
                temp = [dfs(oper_, new_operations,exp) for exp in expressions]
                n = temp[0]
                for i in range(1, len(temp)):
                    n += temp[i]
                result_list.append(n)
        elif oper == "-":
            for oper_ in operations:
                new_operations = list(operations)
                new_operations.remove(oper_)
                temp = [dfs(oper_, new_operations,exp) for exp in expressions]
                n = temp[0]
                for i in range(1, len(temp)):
                    n -= temp[i]
                result_list.append(n)
        else:
            for oper_ in operations:
                new_operations = list(operations)
                new_operations.remove(oper_)
                temp = [dfs(oper_, new_operations,exp) for exp in expressions]
                n = temp[0]
                for i in range(1, len(temp)):
                    n *= temp[i]
                result_list.append(n)

        max = 0
        for r in result_list:
            if abs(max) < abs(r):
                max = r
        return max
                
def solution(expression):
    answer = 0
    
    result_list = []
    operations = ['+','-','*']
    for oper in operations:
        operations = ['+','-','*']
        operations.remove(oper)
        result_list.append(dfs(oper, operations, expression))
        
    answer = -1
    for result in result_list:
        if answer < abs(result):
            answer = abs(result)
    
    return answer